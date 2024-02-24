# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

txt = input()
pattern = r"ab*"
x = re.search(pattern, txt)
# print(x)

# matches = re.findall(pattern, txt)
# for i in matches:
#     print(i)