sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

x = 15
y = 4
print(x + y) #=19
print(x - y) #=11
print(x * y) #=60
print(x / y) #=3.75
print(x % y) #=3
print(x ** y) #=50625
print(x // y) #=3

numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3: #creating variable count and using it in the condition on the same line
    print(f"List has {count} elements")
    
x = 5
print(x > 0 and x < 10) #checking if x is bigger than 0 but smaller than 10

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text) #checking if a substring in the string