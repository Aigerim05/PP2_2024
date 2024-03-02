# Write a Python program to copy the contents of a file to another file

with open('text.txt', 'r') as rf:
    with open('write.txt', 'w') as wf:
        for i in rf:
            wf.write(i)