import pg8000
import csv
import re
from connect import are_we_connected


def filter_by_group(a: str):
	p = are_we_connected()
	q = p.cursor()
	q.execute("SELECT id FROM groups WHERE name = %s", (a,))
	t = q.fetchall()
	if not (bool(t)):
		print(f"The group '{a}' does not exist")
		return None
	q.execute("SELECT * FROM contacts WHERE group_id = %s", (t[0][0],))
	d = q.fetchall()
	for i in d:
		print(i[1] + ":", i[2], i[3], i[4])
	p.close()


def search_by_email(a: str):
	p = are_we_connected()
	q = p.cursor()
	t = True
	q.execute("SELECT email FROM contacts")
	d = q.fetchall()
	for i in d:
		m = re.search(a, str(i[0]))
		if m:
			t = False
			print(i[0])
	if t:
		print("None email is found")
	p.close()

				
def sort_by(a: str, b: int):
	p = are_we_connected()
	q = p.cursor()
	t = ""
	if a == "date added":
		t = "id"
	else:
		t = a
	if b == 0:
		return None
		
	if b > 0:
		match t:
			case "name":
				q.execute("SELECT * FROM contacts ORDER BY name ASC")
			case "birthday":
				q.execute("SELECT * FROM contacts ORDER BY birthday ASC")
			case "id":
				q.execute("SELECT * FROM contacts ORDER BY id ASC")			
			
	elif b < 0:
		match t:
			  	case "name":
			  		q.execute("SELECT * FROM contacts ORDER BY name DESC")
			  	case "birthday":
			  		q.execute("SELECT * FROM contacts ORDER BY birthday DESC")
			  	case "id":
			  		q.execute("SELECT * FROM contacts ORDER BY id DESC")
		
	d = q.fetchall()
	for i in d:
		print(i[1] + ":\t", i[2], i[3], i[4], i[5])
	p.close()

		
def pag_navi():
	p = are_we_connected()
	q = p.cursor()
	q.execute("SELECT COUNT(*) FROM contacts")
	n = q.fetchall()[0][0]
	j = 1
	while True:
		a = input()
		match a:
			case "prev":
				if j != 1:
					j -= 1
				d = query_contacts(1, j)
			case "next":
				if j != n - 1:
					j += 1
				d = query_contacts(1, j)
			case "quit":
				break;
		for i in d:
			print(i[0] + ":\t", i[1], i[2], i[3], i[4])


def add_phone(a, b, bb):
	p = are_we_connected()
	q = p.cursor()
	q.execute("CALL pipis_add_phone(%s, %s, %s)", (a, b, bb))
	p.commit()
	p.close()
	print("The phone is added")


def move_to_group(a, b):
  p = are_we_connected()
  q = p.cursor()
  q.execute("CALL pipis_to_group(%s, %s)", (a, b))
  p.commit()
  p.close()
  print(f"The contact '{a}' is moved to group '{b}'")


def search_contacts(a):
	p = are_we_connected()
	q = p.cursor()
	q.execute("SELECT * FROM pipis_search(%s)", (a,))
	d = q.fetchall()
	if len(d) == 0:
		print("None contacts are found")
		return None
	for i in d:
		print(i[0] + ":\t", i[1], i[2], i[3], i[4])
	p.close()

def csv_inserting(f = "/storage/emulated/0/Download/Practice2/TSIS1/contacts.csv"):
	p = are_we_connected()
	q = p.cursor()
	a = open(f, "r")
	d = csv.DictReader(a)
	dd = list(d)
	d1 = [i["name"] for i in dd]
	d2 = [i["phone_number"] for i in dd]
	d3 = [i["email"] for i in dd]
	d4 = [i["birthday"] for i in dd]
	d5 = [i["group"] for i in dd]
	d6 = [i["type"] for i in dd]
	q.execute("CALL pipislist_insert(%s::text[], %s::text[], %s::text[], %s::date[], %s::text[], %s::text[])", (d1, d2, d3, d4, d5, d6))
	if any(p.notices):
		print(p.notices[0][b'M'].decode())
	p.commit()
	p.close()
	a.close()
	print("The data is inserted\n")
  
def add_contact(a, b):
	p = are_we_connected()
	q = p.cursor()
	q.execute("CALL pipis_insert(%s, %s)", (a, b))
	p.commit()
	p.close()
	print("The contact is added\n")

def update_details(a, b):
	p = are_we_connected()
	q = p.cursor()
	c = input("What data is needed to be updated: ")
	if c == "name":
		c = input("New name: ")
		q.execute("UPDATE contacts SET name = %s WHERE phone_number = %s", (c, b))
		p.commit()	
	elif c == "phone number" or c == "number":
		c = input("New phone number: ")
		q.execute("UPDATE contacts SET phone_number = %s WHERE name = %s", (c, a))
		p.commit()
	p.close()
	print("The details are updated\n")

def filter(a = "name"):
	p = are_we_connected()
	q = p.cursor()
	if a == "name asc" or a == "name":
		q.execute("SELECT * FROM contacts ORDER BY name ASC")
	elif a == "name desc":
		q.execute("SELECT * FROM contacts ORDER BY name DESC")
	elif a == "phone number prefix":
		q.execute("SELECT * FROM contacts ORDER BY phone_number")
	d = q.fetchall()
	for i in d:
		print(i[1] + ":\t" + i[2])
	p.close()

def delete_contact(a):
	p = are_we_connected()
	q = p.cursor()
	q.execute("CALL pipis_delete(%s)", (a,))
	if any(p.notices):
		print(p.notices[0][b'M'].decode())
	else:
		print("The contact is deleted\n")
	p.commit()
	p.close()

def find_contacts(a):
	p = are_we_connected()
	q = p.cursor()
	q.execute("SELECT * FROM pipis_pattern(%s)", (a,))
	d = q.fetchall()
	for i in d:
		print(i[0] + ": ", i[1])
	p.close()
	
def query_contacts(a, b = 0):
	p = are_we_connected()
	q = p.cursor()
	q.execute("SELECT * FROM pipis_query(%s, %s)", (a, b))
	d = q.fetchall()
	p.close()
	return d
	
def view_contacts():
	p = are_we_connected()
	q = p.cursor()
	q.execute("SELECT * FROM contacts")
	d = q.fetchall()
	for i in d:
		print(i[1] + ":\t", i[2], i[3], i[4], i[5])
	p.close()

def view_groups():
	p = are_we_connected()
	q = p.cursor()
	q.execute("SELECT * FROM groups")
	d = q.fetchall()
	for i in d:
		print(i[0], i[1])
	p.close()
	
def view_phones():
	p = are_we_connected()
	q = p.cursor()
	q.execute("SELECT * FROM phones ORDER BY contact_id ASC")
	d = q.fetchall()
	for i in d:
		print(i[1], i[2], i[3])
	p.close()

view_contacts()