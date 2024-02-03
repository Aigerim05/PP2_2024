'''
You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers as an agrument 
and returns only prime numbers from the list.
'''

l = list(map(int, input().split()))

def filter_prime(l):
    for i in l:
        found = True
        for j in range(2, i):
            if(i % j == 0):
                found = False
                break
        if(found):
            print(i)
            
filter_prime(l)