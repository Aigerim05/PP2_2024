'''
Write a Python function that checks whether 
a word or phrase is palindrome or not
'''

s = input()

def is_palindrom(s):
    found = True
    for i in range(0, int(len(s)/2)):
        if(s[i] != s[len(s) - 1 - i]):
            found = False
            break
    print(found)

is_palindrom(s)