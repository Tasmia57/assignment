class BankAccount:
    def __init__(self,starting_balance):
        self._balance=starting_balance

    def deposit(self, amount):
        if amount>0:
            self._balance+=amount
            print("Deposit successful. New balance:",self._balance)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance-=amount
            print("Withdrawal successful. New balance:", self._balance)
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self._balance


account=BankAccount(1000)
account.deposit(500)
print(account.get_balance())
account.withdraw(300)
print(account.get_balance())
account.withdraw(1500)

