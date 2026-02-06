fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) #prints each item

for x in "banana":
  print(x) #prints each symbol of string

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break #exit the loop when x is "banana"

for x in range(6):
  print(x) #prints numbers from 0 to 6 exclusively

adj = ["lovely", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y) #nested for loop