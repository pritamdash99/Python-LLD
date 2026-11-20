# concrete class inheriting interface
from chef import Chef
from order import Order

class PizzaOrder(Order):

    def __init__(self, chef : Chef) -> None:
        self.__chef = chef

    def execute(self):
        print("Pizza Order Placed...")
        self.__chef.cook_pizza()
