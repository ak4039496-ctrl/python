# Author: Amit Gupta
# Date: 15-07-2026
# Description: Stops reading words when 'stop' found

words = ["apple", "banana", "stop", "grape"]
for w in words:
    if w == "stop":
        break
    print(w)
