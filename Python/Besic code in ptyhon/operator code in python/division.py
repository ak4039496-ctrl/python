# Division of two numbers in Python

# Taking input from user
num1 = int(input("Enter first number:- "))
num2 = int(input("Enter second number:- "))

# Performing division
if num2 != 0:
    quotient = num1 / num2
    print("The division of", num1, "by", num2, "is:", quotient)
else:
    print("Error: Division by zero is not allowed.")
