from abc import ABC, abstractmethod
# We know different food items need to be prepared, 
# so we'll create an interface and add an abstract method prepare
class Food(ABC):
    @abstractmethod
    def prepare(self): pass

class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza")

class Burger(Food):
    def prepare(self):
        print("Preparing Burger")

# We don't want to do "pizza = Pizza()"
# This below class Responsible for making objects 
class RestaurantService:
    def create_order(self, food_type : str):
        if food_type == "pizza":
            food = Pizza() #creating pizza object inside class.
        elif food_type == "burger":
            food = Burger() #creating burger object inside class
        else : 
            print("Invalid Food Type")
            return None
        food.prepare() #As food has been identified, the object is created, thus preparation should begin.
    #The aim of this class is to create and return object
        return food

service = RestaurantService()
service.create_order("pizza")
# Preparing Pizza
service.create_order("burger")
# Preparing Burger

"""
This example works but is a BAD EXAMPLE - WHY?
It is TIGHTLY COUPLED - RestaurantService is Tightly Connected to Specific Food Classes.

Restaurant service must know what the user might order first hand.
You'll need to make changes in the core if-else part of service class. 
Defies Open Close Principle, 
    the client code [Restaurant Service] is asking for object, 
    you adding new Food Type, makes you change code inside Client.

Solution - Factory Pattern          Job = Object Creation.

The Factory Pattern moves all object creation logic into 1 central place - the factory class. 
Instead of creating objects directly throughout your code, 
you hand over this responsibility to the factory, 
which decides which specific class object to create based on the request. 

This approach follows the Open / Closed Principle by allowing you to add new food types 
without changing any existing code - 
                            You only update the factory.

What all would it contain?

1. Factory Class - 
The FoodFactory class will hold all the logic for creating different 
    food items based on what the customer orders.
This keeps all creation logic in 1 place. making it simple to add or modify food types.

2. Decoupling - 
The RestaurantService class (client) no longer needs to know how Pizza, Burger or Pasta objects are created,
It simply asks the factory to create the food item and receives it ready to use.

3. Flexibility - 
Adding a new food type (like Biryani) only means updating the factory - 
    the RestaurantService code stays completely unchanged.
"""