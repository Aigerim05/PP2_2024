'''
Define a functino histogram() that takes a list of integers and 
prints a histogram to the screen.
'''

nums = list(map(int, input().split()))

def histogram(l):
    for i in l:
        print('*'*i)

histogram(nums)