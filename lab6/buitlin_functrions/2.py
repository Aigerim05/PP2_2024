# Write a Python program with builtin function that accepts a string and 
# calculate the number of upper case letters and lower case letters

mystring = "Hello WORLD!"
upper = 0
lower = 0


for i in mystring:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1

print("count of uppercase letters: ", upper)
print("count of lowercase letters: ", lower)