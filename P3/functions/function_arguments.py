def s(a, b = 1225): #default parameter
  pass

def p(a, c): #passing list as an argument
	return [i > c for i in a]

def sp(a, b, c):
	return a + b * c

a = [1, 9, 9, 7, 2, 5, 10]
print(p(a, c=6))

print(sp(b=6, a=4, c=3)) #keyword arguments