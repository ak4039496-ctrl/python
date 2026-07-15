# Author:-Amit Kumar
# Date:- 2026-07-10

# Note: Python doesn't have ++ or -- operators. We simulate it inline.
val = 5

# Pre-increment (++val): increase first, then print
val += 1
print(f"Pre-increment (++val) :- {val}")

# Post-increment (val++): print first, then increase
print(f"Post-increment (val++) :- {val}")
val += 1

# Current value of 'val'
print(f"Value of val after post-increment :- {val}")

# Pre-decrement (--val): decrease first, then print
val -= 1
print(f"Pre-decrement (--val) :- {val}")

# Post-decrement (val--): print first, then decrease
print(f"Post-decrement (val--) :- {val}")
val -= 1

# Final value
print(f"Value of val after post-decrement :- {val}")