def sp(a, *b): #*args
  return a + sum(b)
  
def spa(b, **a): #**kwargs
	return a["t"] * a["n"] + b

print(sp(1, 3, 5))

print(spa(4, t=9, n=10))
a = {"t": 9, "n": 10}
print(spa(4, **a)) #unpacking with **