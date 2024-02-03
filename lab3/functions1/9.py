'''
Write a function that computes the 
volume of a sphere given its radius.
'''

r = int(input())

def volume(r):
    return (4/3)*3.14*r*r*r

print(volume(r))