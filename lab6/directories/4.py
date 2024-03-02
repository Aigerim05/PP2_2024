# Write a Python program to count the number of lines in a text file.

with open('text.txt') as f:
    count = 0
    for i in f:
        count += 1

print("Number of lines: ", count)
