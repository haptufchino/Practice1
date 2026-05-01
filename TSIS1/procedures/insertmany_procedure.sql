CREATE OR REPLACE PROCEDURE pipislist_insert(names TEXT[], phoness TEXT[], emails TEXT[], dates DATE[], groupps TEXT[], types TEXT[])
AS $$
DECLARE
  i INT;
  invalid_entries TEXT := '';
BEGIN
  FOR i IN 1..array_length(names, 1) LOOP
    IF phoness[i] !~ '^\+\d{11}$' THEN 
      invalid_entries := invalid_entries || i || ' Name: ' || names[i] || ', Phone: ' || phoness[i] || E'\n';
    ELSE
      IF EXISTS (SELECT 1225 FROM contacts WHERE name = names[i]) THEN
        IF NOT EXISTS (SELECT 1997 FROM groups WHERE name = groupps[i]) THEN
          INSERT INTO groups(name) VALUES (groupps[i]);
        END IF;
        UPDATE contacts SET phone_number = phoness[i], email = emails[i], birthday = dates[i] WHERE name = names[i];
        UPDATE contacts SET group_id = (SELECT id FROM groups WHERE name = groupps[i]) WHERE name = names[i];
        IF NOT EXISTS (SELECT 1997 FROM phones WHERE phone = phoness[i]) THEN
          INSERT INTO phones(contact_id, phone, type) SELECT id, phoness[i], types[i] FROM contacts WHERE phone_number = phoness[i];
        END IF;
      ELSE
        INSERT INTO groups(name) VALUES (groupps[i]);
        INSERT INTO contacts(name, phone_number, email, birthday, group_id) SELECT names[i], phoness[i], emails[i], dates[i], id FROM groups WHERE name = groupps[i];
        INSERT INTO phones(contact_id, phone, type) SELECT id, phoness[i], types[i] FROM contacts WHERE phone_number = phoness[i];
      END IF;
    END IF;
  END LOOP;
  IF invalid_entries <> '' THEN
    RAISE NOTICE E'Invalid entries:\n%', invalid_entries;
  END IF;
END;
$$ LANGUAGE plpgsql;