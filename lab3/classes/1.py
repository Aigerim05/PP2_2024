'''
Define a class which has at least two methods: getString: to get a string from console input 
printString: to print the string in upper case.
'''

class InputOutput:
    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s
    
    def getString(self):
        return self.s
    
    def printString(self):
        print(self.s.upper())
    
s1 = InputOutput(input())
print(s1)
# s1.printString()