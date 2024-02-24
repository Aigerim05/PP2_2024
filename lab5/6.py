# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

txt = input()

pattern = "\s|,|\."

y = re.sub(pattern, ":", txt)

print(y)


