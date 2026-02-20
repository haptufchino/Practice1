a = [1, 9, 9, 7, "big", "shot", [1, 2], (2, 5), "on a late night"]
b = list(filter(lambda x: type(x) == type(str()), a)) #filters on a condition if data type of element is string
print(b)