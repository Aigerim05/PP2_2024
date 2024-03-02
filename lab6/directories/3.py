# Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path.

import os

mypath = "/Users/aigerim.darmeshgmail.com/Documents/pp2/lab6"

if os.path.exists(mypath):
    splitted = os.path.split(mypath)
    print("Directory portion: ", splitted[0])
    print("Filename: ", splitted[1])
else:
    print("path does not exist")


# variant - 2
# if os.path.exists(mypath):
#     print("Directory portion: ", os.path.dirname(mypath))
#     print("Filename: ", os.path.basename(mypath))
# else:
#     print("does not exist")
