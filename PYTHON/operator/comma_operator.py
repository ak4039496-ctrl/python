# Author:-Amit Kumar
# Date:- 2026-07-10

# Note: Python doesn't support sequential multi-assignment inside parentheses like C.
# We explicitly evaluate them line by line for clarity.

a = 5        # Step 1
b = 10       # Step 2
c = a + b    # Step 3 (Final computation assigned to c)

# Print results
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")