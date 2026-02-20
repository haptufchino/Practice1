class big_shot:
	def __init__(self, kromer, glasses, soul, is_successful, hyperlink="blocked"):
		self.kromer = kromer #int
		self.glasses = glasses #string
		self.soul = soul #int
		self.is_successful = is_successful #boolean
		self.hyperlink = hyperlink #string
	def __str__(self):
		b = "not successful"
		if self.is_successful:
			b = "successful"
		return f"\n[{self.kromer} kromer,\n{self.glasses} glasses,\nthe number of souls: {self.soul},\n{b},\nhyperlink={self.hyperlink}]\n"
	def chance(self): #returns a value depending on the content of characteristics
		c = 0
		if self.glasses == "pink and yellow" or self.glasses == "yellow and pink":
			c += 35
		if self.kromer >= 1997:
			c += 20
		if self.is_successful == True:
			c += 30
		if self.is_successful != "blocked":
			c += 25
		if self.soul == 2:
			c = 100
		return c
	def verdict(self): #prints a message using previous method
	  c = self.chance()
	  if c < 100:
	  	print(f"There is a {c}% chance you can be a big shot")
	  else:
	  	print("[NOW'S YOUR CHANCE TO BE A BIG SHOT!']")

k = big_shot(1000, "no", 1, False, "https://youtu.be/dQw4w9WgXcQ?si=V9T5xGiAWgyfsYtP")
s = big_shot(1997, "pink and yellow", 2, True)
print("k:", k)
k.verdict(); print()
print("s:", s)
s.verdict()