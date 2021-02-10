#Question 1
#Write a program to print the following pattern
#1
#22
#333
#4444
#55555

for i in range(6):
    for j in range(i):
        print(i, end=" ")  
    print(" ")


#Question 2
#Write a Python program to add two numbers using class and object.
#(Take both numbers as input from the user)
class Add:

    def sum(self, a, b):
        s = a + b
        return s


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

obj = Add()
s = obj.sum(a, b)

print("Sum is:", s)


#Question 3
#Define a function swap that should swap two values and print the swapped variables outside the
#swap function.
def swap(a, b):
    temp = a
    a = b
    b = temp
    
    print("After Swapping two Number: num1 = {0} and num2 = {1}".format(a, b))
 
num1 = float(input(" Please Enter the First Value : "))
num2 = float(input(" Please Enter the Second Value : "))

print("Before Swapping two Number: num1 = {0} and num2 = {1}".format(num1, num2))
swap(num1, num2)
