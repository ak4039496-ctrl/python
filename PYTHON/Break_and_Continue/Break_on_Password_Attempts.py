# Author: Amit Gupta
# Date: 15-07-2026
# Description: Stops after 3 failed attempts

attempts = 0
while True:
    pwd = input("Enter password:-")
    if pwd == "Amit@123":
        print("Access granted")
        break
    attempts += 1
    if attempts == 3:
        print("Too many attempts")
        break
