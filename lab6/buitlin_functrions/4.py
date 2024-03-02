# Write a Python program that invoke square root function after specific milliseconds.

import time

seconds = 25100
milliseconds = 2123

time.sleep(milliseconds / 1000)  
square_root = pow(seconds, 0.5)
print(f"Square root of {seconds} after {milliseconds} milliseconds is {square_root}")


