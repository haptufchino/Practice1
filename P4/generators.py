def sq(n):
	for i in range(1, n + 1):
		yield i ** 2

def ev(n):
  for i in range(0, n + 1, 2):
  	yield i

def iter_3_4(n):
	for i in range(0, n + 1):
		if i % 12 == 0:
			yield i

def squares(a, b):
	for i in range(a, b + 1):
		yield i ** 2
		
def decr(n):
	for i in range(n, 0 - 1, -1):
		yield i

a = int(input()) # ev function
print(",".join([str(i) for i in ev(a)]))

a = int(input()) #squares function
b = int(input())
for i in squares(a, b):
	print(i, end=" ")