# Waiter class just needs to take order and place order.
from order import Order
class Waiter:
    def take_Order(self, order : Order):
        order.execute()
