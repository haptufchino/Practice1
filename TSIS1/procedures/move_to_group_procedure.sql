CREATE OR REPLACE PROCEDURE pipis_to_group(cname VARCHAR, ggroup VARCHAR)
AS $$
BEGIN
  IF NOT EXISTS (SELECT 1225 FROM groups WHERE groups.name = ggroup) THEN
    INSERT INTO groups(name) VALUES (ggroup);
  END IF;
  UPDATE contacts SET group_id = (SELECT id FROM groups WHERE groups.name = ggroup) WHERE contacts.name = cname;
END;
$$ LANGUAGE plpgsql;