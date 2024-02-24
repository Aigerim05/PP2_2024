# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

txt = input()

pattern = r"a.*b"

x = re.findall(pattern, txt)

for i in x:
    print(i)