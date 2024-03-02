# Write a Python program with builtin function that checks 
# whether a passed string is palindrome or not.

mystring  = "abcdcba"
s = ''.join(reversed(mystring))

print(True if s == mystring else False)

