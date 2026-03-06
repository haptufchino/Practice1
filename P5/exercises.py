import re

a = input() # 1
b = re.match(r"ab+", a)
if b:
	print("Match")
else:
	print("No match")

a = input() # 2
b = re.match(r"ab{2,3}", a)
if b:
	print("Match")
else:
	print("No match")

a = input() # 3
b = re.findall(r"[a-z]+_[a-z]+", a)
print(" ".join(b))

a = input() # 4
b = re.findall(r"[A-Z]{1}[a-z]{1,}", a)
print(" ".join(b))

a = input() # 5
b = re.match(r"^a.*b$", a)
if b:
	print("Match")
else:
	print("No match")

a = input() # 6
b = re.sub(r"[.,\s]", ";", a)
print(b)

a = input() # 7
b = re.sub(r"_[a-z]{1,}", lambda x: x.group()[1:].capitalize(), a)
print(b)

a = input() # 8
b = re.split(r"(?=[A-Z])", a)
del b[0]
print(b)

a = input() # 9
b = re.split(r"(?=[A-Z])", a)
del b[0]
b = " ".join(b)
print(b)

a = input() # 10
b = re.split(r"(?=[A-Z])", a)
del b[0]
b = "_".join([i.lower() for i in b])
print(b)