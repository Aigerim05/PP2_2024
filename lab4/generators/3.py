# Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and n.

n = int (input())

def divisible(n):
    for i in range(0, n + 1):
        if i%12 == 0:
            yield i

mynums = divisible(n)
for i in mynums:
    print(i)
