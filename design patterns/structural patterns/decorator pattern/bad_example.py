from abc import ABC, abstractmethod

# We create an interface Beverage
class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str: pass

    @abstractmethod
    def get_cost(self) -> int : pass

class Coffee(Beverage):

    def get_description(self) -> str:
        return "Plain Coffee"

    def get_cost(self) -> int:
        return 20

class CoffeeWithMilk(Coffee):
    def get_description(self) -> str:
        return "Plain Coffee With Milk"

    def get_cost(self) -> int:
        return 30

coffee1 = Coffee()
print(coffee1.get_description())
print("Rs.",coffee1.get_cost())
# Plain Coffee
# Rs. 20

coffeeWithMilk = CoffeeWithMilk()
print(coffeeWithMilk.get_description())
print("Rs.",coffeeWithMilk.get_cost())
# Plain Coffee With Milk
# Rs. 30

"""
If we add x more sub classes we'll need 2 ^ x combinations = sub-class explosion
This is neither maintainable, nor scalable.

"""

