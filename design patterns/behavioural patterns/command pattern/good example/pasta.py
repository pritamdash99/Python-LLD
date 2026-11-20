# concrete class inheriting interface
from chef import Chef
from order import Order

class PastaOrder(Order):

    def __init__(self, chef : Chef) -> None:
        self.__chef = chef

    def execute(self):
        print("Pasta Order Placed...")
        self.__chef.cook_pasta()