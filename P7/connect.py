import pg8000
from config import data

def are_we_connected():
	con = pg8000.connect(**data)
	return con