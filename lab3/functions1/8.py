'''
Write a function that takes in a 
list of integers and returns True if it contains 007 in order
'''
nums = list(map(int, input().split()))

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
        
spy_game(nums)