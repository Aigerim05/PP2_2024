# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import os

order = "ABCDEFGHIJKLMNOPQRSTWVUXYZ"

for i in order:
    os.mkdir((f'{i}.txt'))