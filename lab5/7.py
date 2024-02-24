# Write a python program to convert snake case string to camel case string.
#snakecase: my_string
#CamelCase: MyString

import re

txt = input()
newtxt = txt.capitalize()
pattern = r"_([a-z])"

result = re.sub(pattern, lambda mymatch: mymatch.group(1).upper(), newtxt)
print(result)
    
#group(0) - is entire match with underscore
#group(1) - is math of only lowercase letter
#capitalize() - converts only the first letter capital