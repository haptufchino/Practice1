def spt(a):
	return lambda x: a * x #returns a lambda function

spt_10 = spt(10)
spt_5 = spt(5)
print(spt_10(7))
print(spt_5(7)) #calls lambda function