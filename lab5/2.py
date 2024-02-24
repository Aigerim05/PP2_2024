# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

txt = "afcfsfdweabfd;labbbb"
pattern = r"abb|abbb"
x = re.search(pattern, txt)
# matches = re.findall(pattern, txt)
# for i in matches:
#     print(i)