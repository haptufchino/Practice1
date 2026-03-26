import pg8000
import csv
from connect import are_we_connected

def csv_inserting(f = "/storage/emulated/0/Download/Practice2/P7/contacts.csv"):
	p = are_we_connected()
	q = p.cursor()
	a = open(f, "r")
	d = csv.DictReader(a)
	for t in d:
	 q.execute("INSERT INTO contacts (name, phone_number) VALUES (%s, %s)", (t["name"], t["phone_number"]))
	p.commit()
	p.close()
	a.close()
	print("The data is inserted\n")
  
def add_contact(a, b):
	p = are_we_connected()
	q = p.cursor()
	q.execute("INSERT INTO contacts (name, phone_number) VALUES (%s, %s)", (a, b))
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

def delete_contact(**a):
	p = are_we_connected()
	q = p.cursor()
	b, bb = a.get("name"), a.get("phone_number")
	if b != None:
		q.execute("DELETE FROM contacts WHERE name = %s", (b,))
		p.commit()
	elif bb != None:
		q.execute("DELETE FROM contacts WHERE phone_number=%s", (bb,))
		p.commit()
	p.close()
	print("The contact is deleted\n")

def view_contacts():
	p = are_we_connected()
	q = p.cursor()
	q.execute("SELECT * FROM contacts")
	d = q.fetchall()
	for i in d:
		print(i[1] + ":\t" + i[2])
	p.close()
	
view_contacts()