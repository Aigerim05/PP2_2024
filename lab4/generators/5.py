# Implement a generator that returns all numbers from (n) down to 0.

def gen(n):
    for i in range(n, -1, -1):
        yield i

mygen = gen(10)

for i in mygen:
    print(i)