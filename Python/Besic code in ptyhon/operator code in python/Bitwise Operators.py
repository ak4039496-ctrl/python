# basic_bitwise_operators.py
# Author: Amit Gupta
# Description: Demonstration of Python bitwise operators

a = 5   # Binary: 0101
b = 3   # Binary: 0011

print("a & b  →", a & b)   # AND → 0001 → 1
print("a | b  →", a | b)   # OR  → 0111 → 7
print("a ^ b  →", a ^ b)   # XOR → 0110 → 6
print("~a     →", ~a)      # NOT → -(a+1) → -6
print("a << 1 →", a << 1)  # Left shift → 1010 → 10
print("a >> 1 →", a >> 1)  # Right shift → 0010 → 2
