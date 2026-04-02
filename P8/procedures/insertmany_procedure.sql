CREATE OR REPLACE PROCEDURE pipislist_insert(names TEXT[], phones TEXT[])
AS $$
DECLARE
  i INT;
  invalid_entries TEXT := '';
BEGIN
  FOR i IN 1..array_length(names, 1) LOOP
    IF phones[i] !~ '^\+\d{11}$' THEN 
      invalid_entries := invalid_entries || i || ' Name: ' || names[i] || ', Phone: ' || phones[i] || E'\n';
    ELSE
      IF EXISTS (SELECT 1225 FROM contacts WHERE name = names[i]) THEN
        UPDATE contacts SET phone_number = phones[i] where name = names[i];
      ELSIF EXISTS (SELECT 1225 FROM contacts WHERE phone_number = phones[i]) THEN
        UPDATE contacts SET name = names[i] WHERE phone_number = phones[i];
      ELSE
        INSERT INTO contacts(name, phone_number) VALUES (names[i], phones[i]);
      END IF;
    END IF;
  END LOOP;
  IF invalid_entries <> '' THEN
    RAISE NOTICE E'Invalid entries:\n%', invalid_entries;
  END IF;
END;
$$ LANGUAGE plpgsql;