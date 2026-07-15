# Author:-Amit Kumar
# Date:- 2026-07-10

# Input a number
a = int(input("Enter a number:- "))

# In Python, assigning a variable to another creates a reference (similar to a pointer)
ptr = a

# Print value of 'a' directly
print("Value of a =>", a)

# Print address of 'a' using hex() and id() to mimic the & operator
print("Address of a =>", hex(id(a)))

# Print value of 'a' using the reference variable
print("Value of a using pointer reference =>", ptr)