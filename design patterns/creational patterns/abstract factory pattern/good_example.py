from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self): pass

# We start by abstracting the cuisine parts - starters, main & deserts & 
# getting them inherited by respective food items.

class Starter(ABC):
    @abstractmethod
    def prepare(self): pass

class MainCourse(ABC):
    @abstractmethod
    def prepare(self): pass

class Desert(ABC):
    @abstractmethod
    def prepare(self): pass

# ======== North Indian Dishes =======

class PaneerTikka(Starter):
    def prepare(self):
        print("Preparing Paneer Tikka (North Indian Starter)")

class ButterChicken(MainCourse):
    def prepare(self):
        print("Preparing Butter Chicken (North Indian Main Course)")

class GulabJamun(Desert):
    def prepare(self):
        print("Preparing Gulab Jamun (North Indian Desert)")

# ======== South Indian Dishes =======

class MeduVada(Starter):
    def prepare(self):
        print("Preparing Medu Vada (South Indian Starter)")

class Dossa(MainCourse):
    def prepare(self):
        print("Preparing Dossa (South Indian Main Course)")

class Payasam(Desert):
    def prepare(self):
        print("Preparing Payasam (South Indian Desert)")

# ======== Chinese Dishes =======

class SpringRolls(Starter):
    def prepare(self):
        print("Preparing Spring Rolls (Chinese Starter)")

class FriedRice(MainCourse):
    def prepare(self):
        print("Preparing Fried Rice (Chinese Main Course)")

class FortuneCookie(Desert):
    def prepare(self):
        print("Preparing Fortune Cookie (Chinese Desert)")

#Our factory won't make Food, It'll make cuisines.
class CuisineFactory(ABC):
    @abstractmethod
    def createStarter(self) -> Starter: pass

    @abstractmethod
    def createMainCourse(self) -> MainCourse : pass

    @abstractmethod
    def createDesert(self) -> Desert : pass


class NorthIndianCuisine(CuisineFactory):
    def createStarter(self) -> Starter: 
        return PaneerTikka()

    def createMainCourse(self) -> MainCourse : 
        return ButterChicken()

    def createDesert(self) -> Desert : 
        return GulabJamun()

class RestaurantService:    #Job = Create Meal / Take Order

    def __init__(self, cuisine_type : CuisineFactory) -> None:
        #This takes a cuisine type at initiation
        self.__factory = cuisine_type

    def create_meal(self):
        # starts creating respective meals.
        starter = self.__factory.createStarter()
        main_course = self.__factory.createMainCourse()
        desert = self.__factory.createDesert()

        #Once we have the orders, we prepare respective meals.
        starter.prepare()
        main_course.prepare()
        desert.prepare()
        #Done
    
    def changeCuisine(self, newCuisine : CuisineFactory) -> None:
        self.__factory = newCuisine
    
northIndian = NorthIndianCuisine()
service = RestaurantService(northIndian)
service.create_meal()

# Preparing Paneer Tikka (North Indian Starter)
# Preparing Butter Chicken (North Indian Main Course)
# Preparing Gulab Jamun (North Indian Desert)

class SouthIndianCuisine(CuisineFactory):
    def createStarter(self) -> Starter: 
        return MeduVada()

    def createMainCourse(self) -> MainCourse : 
        return Dossa()

    def createDesert(self) -> Desert : 
        return Payasam()

class ChineseCuisine(CuisineFactory):
    def createStarter(self) -> Starter: 
        return SpringRolls()

    def createMainCourse(self) -> MainCourse : 
        return FriedRice()

    def createDesert(self) -> Desert : 
        return FortuneCookie()

southIndian = SouthIndianCuisine()
service.changeCuisine(southIndian)
service.create_meal()
# Preparing Medu Vada (South Indian Starter)
# Preparing Dossa (South Indian Main Course)
# Preparing Payasam (South Indian Desert)

chinese = ChineseCuisine()
service.changeCuisine(chinese)
service.create_meal()
# Preparing Spring Rolls (Chinese Starter)
# Preparing Fried Rice (Chinese Main Course)
# Preparing Fortune Cookie (Chinese Desert)

# Thus we no longer need to make any changes inside the client code.