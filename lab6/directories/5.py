# Write a Python program to write a list to a file.
mylist = ['Hello', 'world', '!']

with open('write.txt', 'w') as f:
    f.write(str(mylist))