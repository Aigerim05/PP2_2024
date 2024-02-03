'''
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
'''
nums = list(map(int, input().split()))

def has_33(nums):
    found = False
    for i in range(len(nums)):
        if(nums[i] == 3 and nums[i + 1] == 3):
            found = True
            break
    print(found)

has_33(nums) 