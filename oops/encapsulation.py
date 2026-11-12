"""
ENCAPSULATION - 

Encapsulation is about protecting the internal data of a class.
You control what the outside world CAN SEE and what it CANNOT.
This prevents accidental modification of important data.

- Data and methods that operate on that data are bundled together inside a class.
- Sensitive data is marked [PRIVATE] so it can't be accesses directly from outside. 
- Access is given through controlled methods called GETTERS and SETTERS
- Makes code more secure and predictable

Real Life Example - 
In ATM machine you 
can check balance and withdraw, but
cannot access the bank's internal system directly.
"""

class Bank:
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
        
    def deposit(self, amount:int) ->None:
        self.balance += amount
        print(f"Amount deposited = {amount}, balance = {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdraw Declined : Insufficient Fund, Current Balance = {self.balance}")
        else:
            self.balance -= amount
            print(f"{amount} Withdraw Success, Balance = {self.balance}")

acc = Bank("Pritam", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(3000)
# Amount deposited = 500, balance = 1500
# 300 Withdraw Success, Balance = 1200
# Withdraw Declined : Insufficient Fund, Current Balance = 1200

# CURRENT ISSUE - the "balance" attribute is public, so object.balance can be set outside the class by anyone.
acc.balance = 10000
acc.withdraw(3000)
# 3000 Withdraw Success, Balance = 7000
# This should not be possible. The balance attribute should be "Private", should only be visible not editable by outside world.
