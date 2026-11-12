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

#----------------------------
# Inorder to make any attribute PRIVATE - just add "__" as prefix, so "self.__balance"

class New_Bank:
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.__balance = balance #This attribute is now private aka immutable outside said class.
        
    def deposit(self, amount:int) ->None:
        self.__balance += amount
        print(f"Amount deposited = {amount}, balance = {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Withdraw Declined : Insufficient Fund, Current Balance = {self.__balance}")
        else:
            self.__balance -= amount
            print(f"{amount} Withdraw Success, Balance = {self.__balance}")

acc_new = New_Bank("Pritam", 1000)
acc_new.__balance = 100000
acc_new.withdraw(3000)
# Withdraw Declined : Insufficient Fund, Current Balance = 1000
# The balance attribute couldnot be accessed from outside class.
# So, how to print balance attribute now that it is inaccessible via object.balance
# You use "getters" aka attribute_getting_methods() to get private attributes and 
# "setters" aka attribute_setting_methods() to set private attributes. 

#----------------------------------

class Better_Bank:
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.__balance = balance #This attribute is now private aka immutable outside said class.
        
    def deposit(self, amount:int) ->None:
        self.__balance += amount
        print(f"Amount deposited = {amount}, balance = {self.__balance}")

    def withdraw(self, amount:int) ->None:
        if amount > self.__balance:
            print(f"Withdraw Declined : Insufficient Fund, Current Balance = {self.__balance}")
        else:
            self.__balance -= amount
            print(f"{amount} Withdraw Success, Balance = {self.__balance}")

    def get_balance(self) -> None:
        #This is a getter function
        print(f"Current Balance = {self.__balance}")

    def set_balance(self,new_amount:int) -> None:
        #This is a just a setter example to set balance, in real world, balance is not set like this.
        self.__balance = new_amount

better_acc = Better_Bank("Pritam", 2500)
better_acc.get_balance()
#Current Balance = 2500

#----------------------------------
#You can also make a method private by adding "__" as prefix
#Let's implement a private function to check if server is live [obviously internal work]

class Bankify:
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.__balance = balance #This attribute is now private aka immutable outside said class.

    def __isServerLive(self) -> bool: #This function is private.
            return True
        
    def deposit(self, amount:int) ->None:
        if self.__isServerLive:
            self.__balance += amount
            print(f"Amount deposited = {amount}, balance = {self.__balance}")
        else: 
            print("Server Down, Deposit Failed")

    def withdraw(self, amount:int) ->None:
        if self.__isServerLive:
            if amount > self.__balance:
                print(f"Withdraw Declined : Insufficient Fund, Current Balance = {self.__balance}")
            else:
                self.__balance -= amount
                print(f"{amount} Withdraw Success, Balance = {self.__balance}")
        else:
            print("Server Down, Withdraw Failed")

    def get_balance(self) -> None:
        if self.__isServerLive:
            print(f"Current Balance = {self.__balance}")
        else:
            print("Server Down, Balance Check Failed")

    def set_balance(self,new_amount:int) -> None:
        if self.__isServerLive:
            self.__balance = new_amount
        else:
            print("Server Down, Updating Amount Failed")

better_acc = Bankify("Pritam", 3000)
better_acc.get_balance()
# Current Balance = 3000
