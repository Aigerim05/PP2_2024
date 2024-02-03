'''
Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Note: don't use collection set.
'''

l = list(map(int, input().split()))

def unique(l):
    check = []
    for i in l:
        if(i in check):
            continue
        else:
            check.append(i)
    return check

print(unique(l))