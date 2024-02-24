# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
txt = input()
pattern = r"[a-z]+_[a-z]+"

matches = re.findall(pattern, txt)
for i in matches:
    print(i)