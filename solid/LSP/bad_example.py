from abc import ABC, abstractmethod
#Interface BankAccount
class BankAccount(ABC):
    def __init__(self, balance:int) -> None:
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount:int):
        pass

    @abstractmethod
    def deposit(self, amount :int):
        pass

class Savings(BankAccount):
    def __init__(self, balance: int) -> None:
        super().__init__(balance)

    def deposit(self, amount:int):
        self.balance += amount
        print(f"{amount} deposited, current balance : {self.balance}")

    def withdraw(self, amount: int):
        if amount > self.balance : 
            print(f"Insufficient Fund : Balance = {self.balance}")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn, current balance = {self.balance}")

class FixedDeposit(BankAccount):
    def __init__(self, balance: int) -> None:
        super().__init__(balance)

    def deposit(self, amount:int):
        self.balance += amount
        print(f"{amount} deposited, current balance : {self.balance}")

    def withdraw(self, amount: int):
        raise Exception("Cannot withdraw from FD")

savings = Savings(1000)
savings.deposit(200)
savings.withdraw(1500)

# 200 deposited, current balance : 1200
# Insufficient Fund : Balance = 1200

fd = FixedDeposit(3000)
# fd.withdraw(10)
# Exception: Cannot withdraw from FD

# This is a bad example of code following Liskov Substitution Principle
# As here fd.withdraw() is being forced to raise exception insted of steady running.
