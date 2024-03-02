# Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.

import os

mypath = '/Users/aigerim.darmeshgmail.com/Documents/pp2/lab6/directories/deleting_folder/deleting_file.txt'

if os.access(mypath, os.F_OK):
    os.remove(mypath)
