# Author:-Amit Kumar
# Date:- 2026-07-10

# Input a number
num = int(input("Enter a number:- "))

# Nested ternary format in simple beginner Python structure
result = f"{num} is Positive" if num > 0 else (f"{num} is Negative" if num < 0 else f"{num} is Zero")
print(result)