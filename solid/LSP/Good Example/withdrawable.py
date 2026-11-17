from account import Account
from abc import abstractmethod

class Withdrawble_Account(Account):
    def __init__(self, balance: int) -> None:
        super().__init__(balance)

    @abstractmethod
    def withdraw(self, amount:int):
        pass
