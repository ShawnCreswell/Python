class BankAccount:
    # don't forget to add some default values for these parameters!

    accounts = []

    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
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


class user:
    
    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
        self.account = BankAccount(0.02, 400)
        self.savings = BankAccount(.05, 1000)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)

    def make_withdraw(self,amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print("user:", self.first_name, ",", "Checking Account: ", self.account.balance)

    def display_user_balance2(self):
        print("user:", self.first_name, ",", "Saving Account: ", self.savings.balance)

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - (amount)
        return self


user_shawn = user("Shawn", "Creswell", "creswellshawn@gmail.com", 25, False, 0)

user_shawn.display_user_balance()
user_shawn.display_user_balance2()





