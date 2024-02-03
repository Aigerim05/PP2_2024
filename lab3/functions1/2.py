'''Read in a Fahrenheit temperature.
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F – 32)'''

F = int(input())

def convert(x):
    print ((5 / 9) * (x - 32))

convert(F)


