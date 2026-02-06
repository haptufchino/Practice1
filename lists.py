thislist = ["apple", "banana", "cherry"]
print(thislist) #prints the full list

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") #checks if the element apple in the list
  
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #inserts the element watermelon to index 2 and move elements with indexes > 2 further

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #adds element to the list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] #filters the original list on the condition
print(newlist)