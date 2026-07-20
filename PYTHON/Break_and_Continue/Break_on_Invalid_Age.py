# Author: Amit Gupta
# Date: 15-07-2026
# Description: Stops when invalid age entered

ages = [25, 30, -1, 40]
for age in ages:
    if age < 0:
        print("Invalid age found")
        break
    print("Age:", age)
