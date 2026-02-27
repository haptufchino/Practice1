import math

a = int(input()) # 1
b = math.radians(a)
print(b)

h = int(input()) # 2
a = int(input())
b = int(input())
s = (a + b) / 2 * h
print(s)

a = int(input()) # 3
n = int(input())
t = math.tan(math.pi / n)
k = n / (4 * t)
if n < 3:
	print("not a polygon")
elif n == 4:
	print(round(a ** 2 * k))
else:
  print(a ** 2 * k)
  
a = int(input()) # 4
h = int(input())
print(a * h)