# Author: Amit Gupta
# Date: 16-07-2026
# Description: Stops reading lines when 'END' found

lines = ["Line1", "Line2", "END", "Line3"]
for line in lines:
    if line == "END":
        break
    print(line)
