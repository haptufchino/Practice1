number = 15
if number > 0:
  print("The number is positive") # checking if a number is positive
  
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") #elif statement
  
  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") #elif and else statements
  
a = 2
b = 330
print("A") if a > b else print("B") #ternary operator

x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.") #nested conditions