from functools import reduce

a = [1, 2, 3, 4, 5]
b = list(map(lambda x: x * 2, a))
print(b)

c = list(filter(lambda x: x % 2 == 0, a))
print(c)

d = [4, 3, 2, 1]
t = reduce(lambda x, y: x ** y, d)
print(t)