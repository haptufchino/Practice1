class menu:
	m1 = "big tasty"
	m2 = "sanders basket"
	m3 = "happy meal"
	m4 = "chicken mcnuggets"
	m5 = "barbeque"
	m6 = "sprite"
	def show(self):
		print(self.m1, self.m2, self.m3, self.m4, self.m5, self.m6, sep=", ")
		print("What you would like?")

b = menu() #class
b.show() #class method
a = input() #string
c = a.split() #string method
d = b.m1 #access to content of class variable
d = a[0] #access to content of string variable
c = [int(i) for i in c]
for i in range(len(c)):
	if c[i] % 6 == 0:
		c[i] = "m6"
	else:
		c[i] = f"m{c[i]% 6}"
for i in c:
	match i:
		case "m1":
			print(b.m1)
		case "m2":
			print(b.m2)
		case "m3":
			print(b.m3)
		case "m4":
			print(b.m4)
		case "m5":
			print(b.m5)
		case "m6":
			print(b.m6)