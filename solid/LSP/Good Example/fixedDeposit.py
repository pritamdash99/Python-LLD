from account import Account

class FixedDeposit(Account):
    def __init__(self, balance: int) -> None:
        super().__init__(balance)

    def deposit(self, amount: int):
        self.balance += amount
        print(f"Amount Deposited, current balance = {self.balance}")
        
#As we inherited only Account Interface, we don't need to create Withdraw function.

# LSP Preserved this way.
