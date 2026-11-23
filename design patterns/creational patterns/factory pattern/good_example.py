from abc import ABC, abstractmethod
class Food(ABC):
    @abstractmethod
    def prepare(self): pass

class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza")

class Burger(Food):
    def prepare(self):
        print("Preparing Burger")

# We create the FoodFactory to handle object creation
class FoodFactory:
    @staticmethod           #@staticmethod can be called without creating object of the class
    def create_food(food_type: str) -> Food | None:    #staticmethods don't take self as 1st parameter as no object is involved.
        if food_type == "pizza":
            return Pizza()
        elif food_type == "burger":
            return Burger()
        else:
            return None

#this becomes the client which no longer handles different type of food object creations
class RestaurantService:
    def createOrder(self, food_type : str):
        food = FoodFactory().create_food(food_type)
        if food is None:
            print("Cannot prepare requested food")
        else:
            return food.prepare()

service = RestaurantService()
service.createOrder("pizza")
# Preparing Pizza

service.createOrder("burger")
# Preparing Burger

"""
Now, if we have to add another food type = Pasta
so..

class Pasta(Food):
    def prepare(self):
            print("Preparing Pasta")

class FoodFactory:
    @staticmethod           
    def create_food(food_type: str) -> Food | None:   
        if food_type == "pizza":
            return Pizza()
        elif food_type == "burger":
            return Burger()
        elif food_type == "pasta":
            return Pasta()
        else:
            return None 

No more changes in the client class RestaurantService.        
"""
