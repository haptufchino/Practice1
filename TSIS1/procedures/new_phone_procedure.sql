CREATE OR REPLACE PROCEDURE pipis_add_phone (pname VARCHAR, pphone VARCHAR, ptype VARCHAR) AS $$
BEGIN
  INSERT INTO phones(contact_id, phone, type) SELECT id, pphone, ptype FROM contacts WHERE name = pname;
END;
$$ LANGUAGE plpgsql;