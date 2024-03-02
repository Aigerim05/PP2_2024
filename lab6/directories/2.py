# Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path.

import os

mypath = "/Users/aigerim.darmeshgmail.com/Documents/pp2/lab6"

print("Existence: ", os.access(mypath, os.F_OK))
print("Readability: ", os.access(mypath, os.R_OK))
print("Writability: ", os.access(mypath, os.W_OK))
print("Executability: ", os.access(mypath, os.W_OK))