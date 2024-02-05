#task5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        amount = float(input("Amount to be deposited: "))
        self.balance += amount
        

    def withdraw(self):
        amount = float(input("Amount to be withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew: ", amount)
        else:
            print("\n Insufficient balance to withdraw")
    
    def display(self):
        print("\n Net Available Balance of",self.owner, "=",self.balance)
        
o = str(input("Enter the name: "))
b = float(input("Enter the initial capital: "))
a = Account(o, b)

a.deposit()
a.withdraw()
a.display()