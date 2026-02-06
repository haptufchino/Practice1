thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #allows duplicates

tuple1 = ("abc", 34, True, 40, "male") #different data types in a tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) #appending tuple to a tuple

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) #removing item from a tuple by converting it in a list

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red) #unpacking tuple with asterisk