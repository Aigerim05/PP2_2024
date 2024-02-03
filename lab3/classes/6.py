'''
Write a program which can filter prime numbers in a list by using filter function. 
Note: Use lambda to define anonymous functions.
'''

l = list(map(int, input().split()))

def is_prime(x):
    found = True
    for i in range(2, x):
        if(x % i == 0):
            found = False
            break
    return found

a = lambda x: is_prime(x)

new_list = [x for x in l if a(x) == True]

print(new_list)