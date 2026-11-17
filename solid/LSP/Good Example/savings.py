from withdrawable import Withdrawble_Account

class SavingsAccount(Withdrawble_Account):
    def __init__(self, balance: int) -> None:
        super().__init__(balance)

    def deposit(self, amount:int):
        self.balance += amount
        print(f"Amount deposited, current balance = {self.balance}")

    def withdraw(self, amount: int):
        if self.balance < amount:
            print("Cannot withdraw, not enough balance")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn, current balance = {self.balance}")
            