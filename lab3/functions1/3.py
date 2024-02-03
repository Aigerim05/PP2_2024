'''
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have?
'''
numheads = int(input())
numlegs = int(input())

def solve(numheads, numlegs):
    rabbit = (numlegs - 2*numheads)/2
    chicken = numheads - rabbit
    print(int(chicken), int(rabbit))

solve(numheads, numlegs)