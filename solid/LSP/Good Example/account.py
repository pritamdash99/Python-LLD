from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,balance: int) -> None:
        self.balance = balance

    @abstractmethod
    def deposit(self, amount :int):
        pass
