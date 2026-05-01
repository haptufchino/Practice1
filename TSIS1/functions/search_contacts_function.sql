CREATE OR REPLACE FUNCTION pipis_search(a TEXT)
RETURNS TABLE(name VARCHAR, phone_number VARCHAR, email VARCHAR, birthday DATE, group_id INTEGER) as $$
BEGIN
  RETURN QUERY
  SELECT c.name, p.phone, c.email, c.birthday, c.group_id FROM contacts c LEFT JOIN phones p ON p.contact_id = c.id
WHERE c.name ILIKE '%' || a || '%'
   OR c.email ILIKE '%' || a || '%'
   OR p.phone ILIKE '%' || a || '%';
END;
$$ LANGUAGE plpgsql;