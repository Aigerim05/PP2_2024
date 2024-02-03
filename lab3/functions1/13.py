'''
Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. 
'''

import random

print("Hello! What is your name?")
name  = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20. \nTake a guess.")

target_num = random.randint(1, 20)

num = 0
k = 0
while(target_num != num):
    num = int(input())
    if(num < target_num):
        k += 1
        print("Your guess is too low.\nTake a guess.")
    elif(num > target_num):
        k += 1
        print("Your guess is too high.\nTake a guess.")
    else:
        print(f"Good job, {name}! You guessed my number in {k} guesses!")

