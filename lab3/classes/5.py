'''
Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
    
    def withdraw(self, money):
        if(self.balance > money):
            self.balance -= money
        else:
            print("Balance is out of range.")
        
    def show(self):
        print(f"{self.owner} {self.balance}")

client1 = Account("Mike", 23000)
client2 = Account("Bob", 45000)

client1.deposit(10000)
client1.show()

client2.withdraw(50000)
client2.show()

client2.withdraw(20000)
client2.show()