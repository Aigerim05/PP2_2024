# Write a Python program to list only directories, files and all directories, files in a specified path.

import os

mypath = '/Users/aigerim.darmeshgmail.com/Documents/pp2/lab6'
list_of_dirs = [ i for i in os.listdir(mypath) if os.path.isdir(os.path.join(mypath, i))]
list_of_files = [ i for i in os.listdir(mypath) if not os.path.isdir(os.path.join(mypath, i))]
print('Only Directories: ', ' , '.join(list_of_dirs))
print('Only Files: ', ' , '.join(list_of_files))
print('Directories and Files: ',' , '.join(os.listdir(mypath)))
