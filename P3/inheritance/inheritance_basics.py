class old_man:
	def __init__(self, power, wisdom):
		self.power = power
		self.wisdom = wisdom

class darkner(old_man):
	def __init__(self, power, wisdom):
		old_man.__init__(self, power, wisdom)

k = darkner(17, 15)
print(k.wisdom * 2 + k.power)