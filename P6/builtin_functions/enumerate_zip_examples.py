names = ["Gaster", "Noelle", "Susie"]
s = [85, 90, 78]

for i, name in enumerate(names):
    print(i, name)

for name, c in zip(names, s):
    print(name, c)