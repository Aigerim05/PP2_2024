# Implement a generator called squares to yield the square of all numbers from (a) to (b). 
# Test it with a "for" loop and print each of the yielded values.

def squares(a, b):
    for i in range(a, b):
        yield i*i

mysquares = squares(0, 7)

for i in mysquares:
    print(i)