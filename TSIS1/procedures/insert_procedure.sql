CREATE OR REPLACE PROCEDURE pipis_insert (a TEXT, b TEXT)
AS $$
BEGIN
  IF EXISTS(SELECT 1997 FROM contacts WHERE name = a) THEN UPDATE contacts SET phone_number = b WHERE name = a;
  ELSE INSERT INTO contacts (name, phone_number) VALUES (a, b);
  END IF;
END;
$$ LANGUAGE plpgsql;