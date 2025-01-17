# Problem:
# Create a class called BankAccount with the following attributes and methods:

# Attributes: account_holder, balance (default is 0).
# Methods:
# deposit(amount) to add money to the balance.
# withdraw(amount) to deduct money from the balance if sufficient funds are available; otherwise, print "Insufficient funds".
# get_balance() to return the current balance.
# Create an object of BankAccount for "John Doe", deposit $500, withdraw $200, and print the final balance.

class BankAcc:
    balance = 0
    def __init__(self, accholder):

        self.accHolder = accholder
    
    def deposit(self, amount):

        self.amount = amount
        self.balance += self.amount

        return f"The Entered amount is: {self.amount}\n"
    
    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.withdraw

        return f"The Entered amount is: {self.amount}\n"
    
    def get_balance(self):
        return f"Your Curent Balance is : {self.balance}\n"
    

x = input("Enter the Name of User: ")
User = BankAcc(x)

CorAction = False

while CorAction != True:

    action = int(input("1 for Deposit\n2 for Withdraw\n3 for Balance\n4 for Exit\n\nEnter the Choice: "))

    if action == 1:
        depoamt = int(input("Enter the Amount you want to Deposit: "))
        print(User.deposit(depoamt))
    elif action == 2:
        withdamt = int(input("Enter the Amount you want to Withdraw: "))
        print(User.withdraw(withdamt))
    elif action == 3:
        print(User.get_balance())
    elif action == 4:
        CorAction = True
    else:
        print("Invalid Input!!")
        CorAction = False