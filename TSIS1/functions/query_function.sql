CREATE OR REPLACE FUNCTION pipis_query(a INT, b INT)
RETURNS TABLE(name VARCHAR, phone_number VARCHAR, email VARCHAR, birthday DATE, group_id INT) AS $$
BEGIN
  RETURN QUERY 
  SELECT contacts.name, contacts.phone_number, contacts.email, contacts.birthday, contacts.group_id FROM contacts ORDER BY contacts.name LIMIT a OFFSET b;
END;
$$ LANGUAGE plpgsql;