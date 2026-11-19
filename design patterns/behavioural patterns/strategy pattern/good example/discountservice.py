from discountstrategy import DiscountStrategy

class DiscountService:
    def __init__(self, discount_strategy : DiscountStrategy) -> None:
        # by assigning the type of discount_strategy, later in code, autocomplete suggests it's methods and attributes correctly.
        self.__strategy = discount_strategy

    def set_strategy(self, new_strategy : DiscountStrategy):
        self.__strategy = new_strategy

    def process(self):
        # whatever strategy is currently set, we need to call it's calculate function
        self.__strategy.calculate_discount()
