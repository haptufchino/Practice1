import datetime

a = datetime.date.today() # 1
b = datetime.timedelta(days=5)
a -= b
print(a)

a = datetime.date.today() # 2
b = datetime.timedelta(days=1)
print("Yesterday is:", a - b)
print("Today is:", a)
print("Tomorrow is:", a + b)

a = datetime.datetime.now() # 3
a = a.replace(microsecond=0)
print(a)

a = datetime.datetime.strptime(input(), "%Y-%m-%d") # 4
b = datetime.datetime.strptime(input(), "%Y-%m-%d")
c = abs(a - b)
d = str(c.days * 86400)[::-1]
t = ""
for i in range(len(d)):
	t += d[i]
	if i % 3 == 2:
		t += "_"
t = t[::-1]
print(t, "seconds")