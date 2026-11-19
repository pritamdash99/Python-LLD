# Concrete class

from discountstrategy import DiscountStrategy

class Diwali(DiscountStrategy):
    def calculate_discount(self) -> None:
        print("Applying diwali discount of 20%")
