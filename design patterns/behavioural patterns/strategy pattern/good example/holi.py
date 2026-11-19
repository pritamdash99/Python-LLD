# Concrete Class

from discountstrategy import DiscountStrategy

class Holi(DiscountStrategy):
    def calculate_discount(self) -> None:
        print("Applying holi discount of 10%")