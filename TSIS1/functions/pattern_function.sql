CREATE OR REPLACE FUNCTION pipis_pattern(a TEXT)
RETURNS TABLE(name VARCHAR, phone_number VARCHAR) as $$
BEGIN
  RETURN QUERY
  SELECT contacts.name, contacts.phone_number FROM contacts WHERE contacts.name ILIKE '%' || a || '%' OR contacts.phone_number LIKE '%' || a || '%';
END;
$$ LANGUAGE plpgsql;