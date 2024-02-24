# Write a Python program to convert a given camel case string to snake case.

import re

txt = "MakeMeSnake"

pattern = r"([A-Z][a-z]*)"

def to_snake(match):
    return (match.group(1) + "_").lower()

result = re.sub(pattern, to_snake, txt)
print(result)

# -------------------> variant - 2
# result = re.sub(newPattern,r"\1_", txt)
# print(result)

# -------------------> variant with lambda
# result = re.sub(newPattern,lambda match: (match.group(1) + '_').lower(), txt)
# print(result)