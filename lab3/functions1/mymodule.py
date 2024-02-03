def convert_grams_to_ounces(x):
    return 28.3495231 * x

def convert_tempreature(x):
    print ((5 / 9) * (x - 32))

def solve(numheads, numlegs):
    rabbit = (numlegs - 2*numheads)/2
    chicken = numheads - rabbit
    print(int(chicken), int(rabbit))

def filter_prime(l):
    check = []
    found = True
    for i in l:
        for j in range(2, i):
            if(i % j == 0):
                found = False
                break
        if(found): check.append(i)
    return check

            
def reverse(s):
    return s[::-1]

def has_33(nums):
    found = False
    for i in range(len(nums)):
        if(nums[i] == 3 and nums[i + 1] == 3):
            found = True
            break
    print(found)


def spy_game(nums):
    found = False
    check = []
    for i in range(len(nums)):
        if(nums[i] == 0 or nums[i] == 7):
            check.append(nums[i])
    for j in range(len(check) - 2):
        if(check[j] == 0 and check[j + 1] == 0 and check[j + 2] == 7):
            found = True
            break
        else:
            continue
    print(found)

def volume(r):
    return (4/3)*3.14*r*r*r

def unique(l):
    check = []
    for i in l:
        if(i in check):
            continue
        else:
            check.append(i)
    return check

def is_palindrom(s):
    found = True
    for i in range(0, int(len(s)/2)):
        if(s[i] != s[len(s) - 1 - i]):
            found = False
            break
    return found

def histogram(l):
    for i in l:
        print('*'*i)