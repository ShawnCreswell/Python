
class BankAccount:
    # don't forget to add some default values for these parameters!

    accounts = []

    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance  -= amount
        else:
            self.balance -= 5
            print("you dont have that kinda of money bro!")
        return self
        

    def display_account_info(self):
        print("Balance ", self.balance)
        # print("Intrest:", self.int_rate * 100, "%")
        return self
    def yield_interest(self):
        if self.balance <= 0:
            print("Try again next year")
        else:
            self.balance += self.balance * self.int_rate
            self.display_account_info()
        return self

    @classmethod
    def print_all_instnaces(cls):
        for account in cls.accounts:
            print(account.display_account_info())




acct1 = BankAccount(.02, 100).deposit(300).deposit(200).deposit(200).withdraw(500).yield_interest()
acct2 = BankAccount(.03, 100).deposit(1000).deposit(500).withdraw(100).withdraw(150).withdraw(200).withdraw(50).yield_interest()
