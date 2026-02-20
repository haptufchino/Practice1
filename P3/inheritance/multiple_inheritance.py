import time

class gasta:
	def __init__(self, nucb_power):
		self.nucb_power = nucb_power
	def use_nucb(self):
		print("boom", end=" ")
		time.sleep(1)
		for i in range(10 ** 667):
		  print("boom", end=" ", flush=True)
		  time.sleep(0.000004)

class old_man:
	def __init__(self, velocity, wisdom):
		self.velocity = velocity #int
		self.wisdom = wisdom #int
	def dodge(self):
		a = input("Try to attack!")
		if self.velocity >= 130:
			print("Dodged!")
		else:
		  print('["Attack succeded"]')
		time.sleep(1)

class dragon(gasta, old_man):
	def __init__(self, nucb_power, velocity, wisdom, rudeness):
		gasta.__init__(self, nucb_power)
		old_man.__init__(self, velocity, wisdom)
		self.rudeness = rudeness
	def rude_buster(self):
		if self.rudeness >= 50:
			print("Buster!")
			time.sleep(2)

s = dragon(500000, 140, 4000, 80)
s.dodge()
s.rude_buster()
print("I can't bear it anymore!")
s.use_nucb()