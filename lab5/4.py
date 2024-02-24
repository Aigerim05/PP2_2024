# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

txt = input()

pattern = r"[A-Z][a-z]+"

x = re.findall(pattern, txt)

for i in x:
    print(i)