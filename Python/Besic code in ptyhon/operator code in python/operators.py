# Demonstrating Python Operators

a = 10
b = 5

# Arithmetic Operators
print("Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)   # Exponent
print("a // b =", a // b)   # Floor division

# Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operators
print("\nLogical Operators:")
print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b < 0:", a > 0 or b < 0)
print("not(a > b):", not(a > b))

# Assignment Operators
print("\nAssignment Operators:")
x = a
x += b
print("x += b:", x)
x -= b
print("x -= b:", x)
x *= b
print("x *= b:", x)
x /= b
print("x /= b:", x)

# Bitwise Operators
print("\nBitwise Operators:")
print("a & b =", a & b)   # AND
print("a | b =", a | b)   # OR
print("a ^ b =", a ^ b)   # XOR
print("~a =", ~a)         # NOT
print("a << 1 =", a << 1) # Left shift
print("a >> 1 =", a >> 1) # Right shift
