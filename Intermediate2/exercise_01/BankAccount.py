#Reid Witte
#Using w3schools as a reference

class BankAccount:

    def __init__(self, account_name, starting_balance):
        self.name = account_name
        self.balance = starting_balance

    def deposit(self,add):
        self.balance += add

    def withdraw(self,sub):
        self.balance -= sub

    def get_balance(self):
        return self.name + " has a balance of " + str(self.balance)
