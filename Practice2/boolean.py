print(10 > 9)
print(10 == 9)
print(10 < 9) #returning true or false if comparison is right or not

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #defining if b is greater than a or not
  
print(bool("Hello"))
print(bool(15)) #conversion of a data type to boolean

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) #values that return false under conversion

x = 200
print(isinstance(x, int)) #check on certain data type