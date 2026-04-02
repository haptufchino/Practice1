CREATE OR REPLACE FUNCTION pipis_query(a INT, b INT)
RETURNS TABLE(name VARCHAR, phone_number VARCHAR) AS $$
BEGIN
  RETURN QUERY 
  SELECT contacts.name, contacts.phone_number FROM contacts ORDER BY contacts.name LIMIT a OFFSET b;
END;
$$ LANGUAGE plpgsql;