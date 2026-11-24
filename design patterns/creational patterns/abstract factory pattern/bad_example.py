from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):pass

# ======== North Indian Dishes =======

class PaneerTikka(Food):
    def prepare(self):
        print("Preparing Paneer Tikka (North Indian Starter)")

class ButterChicken(Food):
    def prepare(self):
        print("Preparing Butter Chicken (North Indian Main Course)")

class GulabJamun(Food):
    def prepare(self):
        print("Preparing Gulab Jamun (North Indian Desert)")

# ======== South Indian Dishes =======

class MeduVada(Food):
    def prepare(self):
        print("Preparing Medu Vada (South Indian Starter)")

class Dossa(Food):
    def prepare(self):
        print("Preparing Dossa (South Indian Main Course)")

class Payasam(Food):
    def prepare(self):
        print("Preparing Payasam (South Indian Desert)")

# ======== Chinese Dishes =======

class SpringRolls(Food):
    def prepare(self):
        print("Preparing Spring Rolls (Chinese Starter)")

class FriedRice(Food):
    def prepare(self):
        print("Preparing Fried Rice (Chinese Main Course)")

class FortuneCookie(Food):
    def prepare(self):
        print("Preparing Fortune Cookie (Chinese Desert)")

class RestaurantService:                         #Objects are being created inside Client = Tight Coupling
    def create_meal(self, cuisine_type : str):
        if cuisine_type == "north_indian":
            starter = PaneerTikka()
            main_course = ButterChicken()
            dessert = GulabJamun()
        elif cuisine_type == "south_indian":
            starter = MeduVada()
            main_course = Dossa()
            dessert = Payasam()
        elif cuisine_type == "chinese":
            starter = SpringRolls()
            main_course = FriedRice()
            dessert = FortuneCookie()
        else:
            print("Cuisine Not Available!")
            return None

        #Prepare the meal 
        starter.prepare()
        main_course.prepare()
        dessert.prepare()

service = RestaurantService()
service.create_meal("north_indian")
service.create_meal("south_indian")
service.create_meal("chinese")

"""
Preparing Paneer Tikka (North Indian Starter)
Preparing Butter Chicken (North Indian Main Course)
Preparing Gulab Jamun (North Indian Desert)
Preparing Medu Vada (South Indian Starter)
Preparing Dossa (South Indian Main Course)
Preparing Payasam (South Indian Desert)
Preparing Spring Rolls (Chinese Starter)
Preparing Fried Rice (Chinese Main Course)
Preparing Fortune Cookie (Chinese Desert)


If we need to add another cuisine - 
    we'll need to make changes inside client's if-elif statements &
    create object inside Client.

It's a violation of open close principle.

"""
        