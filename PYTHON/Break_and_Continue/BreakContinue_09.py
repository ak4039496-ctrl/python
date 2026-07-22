# Author: Amit Gupta
# Date: 15-07-2026
# Program: Break on Prime Found
# Description: Stops when first prime number found

nums = [4, 6, 8, 9, 11, 15]
for n in nums:
    if all(n % i != 0 for i in range(2, n)):
        print("First prime:", n)
        break
