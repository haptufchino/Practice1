class friend:
	def __init__(self, vision, power, knowledge):
		self.vision = vision
		self.power = power
		self.knowledge = knowledge

class darkner(friend):
	def __init__(self, vision, power, knowledge, name):
		super().__init__(vision, power, knowledge)
		self.name = name
	def say(self):
		print(self.name)

k = darkner(6, 4, 7, "kris")
k.say()