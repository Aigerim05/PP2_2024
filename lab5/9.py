# Write a Python program to insert spaces between words starting with capital letters.

import re

def replF(obj):
    return obj.group('FL') + ' '

txt = "MyWordNeedsSpace"

newPattern = r"(?P<FL>[A-Z][a-z]+)"

result = re.sub(newPattern ,replF, txt)
print(result)

# -------------------> variant - 2
# result = re.sub(newPattern,r"\1 ", txt)
# print(result)

# ------------------> variant with lambda function 

# newPattern = r"(?P<FL>[A-Z][a-z]+)"
# result = re.sub(newPattern , lambda match: match.group("FL") + ' ', txt)
# print(result)