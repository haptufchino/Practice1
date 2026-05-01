CREATE OR REPLACE PROCEDURE pipis_delete(a TEXT)
AS $$
BEGIN
  IF EXISTS(SELECT 1997 FROM CONTACTS WHERE name = a OR phone_number = a) THEN
    DELETE FROM contacts WHERE name = a OR phone_number = a;
  ELSE
    RAISE NOTICE 'Cannot delete';
  END IF;
END;
$$ LANGUAGE plpgsql;