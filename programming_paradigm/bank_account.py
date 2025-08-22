class BankAccount:
    def __init__(self, initial_balance=0):
        # start with an initial balance (default is 0)
        self.account_balance = initial_balance

    def deposit(self, amount):
        # add money to the balance
        self.account_balance += amount

    def withdraw(self, amount):
        # check if there is enough money
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # show balance in a simple way
        print("Current Balance:", self.account_balance)
