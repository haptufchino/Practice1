class em:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
	def notify(self):
		print(f"{name} has salary of {salary}$")

class cashier(em):
	def __init__(self, name, salary, bon):
		super().__init__(name, salary)
		self.bon = bon
	def notify(self):
		print(f"{self.name} has salary of {self.salary * self.bon}$")

sq = cashier("squid", 5, 1.01)
sq.notify()