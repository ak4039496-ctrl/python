# Author: Amit Gupta
# Date: 15-07-2026
# Program: Break on Negative Input
# Stops when user enters negative number

while True:
    num = int(input("Enter number:- "))
    if num < 0:
        print("Stopped on negative input")
        break
    print("You entered:", num)
