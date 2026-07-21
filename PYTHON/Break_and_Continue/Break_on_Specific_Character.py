# Author: Amit Gupta
# Date: 16-07-2026
# Description: Stops loop when character 'x' found

text = "hello world x python"
for ch in text:
    if ch == "x":
        break
    print(ch, end="")
