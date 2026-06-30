
# basic_identity_operators.py
# Author: Amit Gupta
# Description: Demonstration of Python identity operators

a = [1, 2]
b = [1, 2]
c = a

print("a is b      →", a is b)      # False (different objects, even if values same)
print("a is c      →", a is c)      # True (same object reference)
print("a is not b  →", a is not b)  # True (a and b are not same object)
