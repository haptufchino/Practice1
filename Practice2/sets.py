thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)  #Access to items

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)  #adding item to a set
  
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) #extending set with a container

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset) #removing random item from a set

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) #frozen set