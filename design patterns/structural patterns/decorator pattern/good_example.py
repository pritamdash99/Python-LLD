from abc import ABC, abstractmethod

# We create an interface Beverage
class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str : pass

    @abstractmethod
    def get_cost(self) -> int : pass

class Coffee(Beverage):
    def get_description(self) -> str:
        return "Plain Coffee"
    def get_cost(self) -> int:
        return 20

# We start with AddOnDecorator

class AddOnDecorator(Beverage):
    def __init__(self, coffee: Beverage) -> None:
        self.__coffee = coffee

    #Returning coffee values as inheriting classes will override these functions
    def get_description(self) -> str: 
        return self.__coffee.get_description()  
     
    def get_cost(self) -> int : 
        return self.__coffee.get_cost()

    def get_coffee(self) -> Beverage:
        return self.__coffee

class MilkDecorator(AddOnDecorator):
    def get_description(self):
        return self.get_coffee().get_description() + ", Milk"
    def get_cost(self) -> int:
        return self.get_coffee().get_cost() + 20

class WhippedCreamDecorator(AddOnDecorator):
    def get_description(self):
        return self.get_coffee().get_description() + ", Whipped Cream"
    def get_cost(self) -> int:
        return self.get_coffee().get_cost() + 50

class SugarDecorator(AddOnDecorator):
    def get_description(self):
        return self.get_coffee().get_description() + ", Sugar"
    def get_cost(self) -> int:
        return self.get_coffee().get_cost() + 5

# Now we make our coffee  
print("Menu -->")
coffee = Coffee()
print(coffee.get_description())
print(coffee.get_cost())

print("--------------")
coffee = MilkDecorator(coffee)
print(coffee.get_description())
print(coffee.get_cost())

print("--------------")
coffee = WhippedCreamDecorator(coffee)
print(coffee.get_description())
print(coffee.get_cost())

print("--------------")
coffee = SugarDecorator(coffee)
print(coffee.get_description())
print(coffee.get_cost())

"""
Menu -->
Plain Coffee
20
--------------
Plain Coffee, Milk
40
--------------
Plain Coffee, Milk, Whipped Cream
90
--------------
Plain Coffee, Milk, Whipped Cream, Sugar
95
"""