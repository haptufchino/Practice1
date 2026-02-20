def spm(a): #defining a function
  print(f"Hello, {a}") #a procedure that does not return value

def tenn(a, b):
	return a + b * b #a function that returns value
	
def s(): #a function without argument
  print(1997)

a = input()
spm(a) #calling the procedure
spm(a)
spm(a) #can be called multiple times

a = int(input())
b = int(input())
c = tenn(a, b) #calling the function
print(c)

s()