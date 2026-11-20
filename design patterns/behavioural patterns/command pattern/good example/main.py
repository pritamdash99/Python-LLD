# We use this execute logic & create objects

from chef import Chef
from waiter import Waiter
from pasta import PastaOrder
from pizza import PizzaOrder

#Chef needs to exist in real life
chef = Chef()

#Orders need to exist in real life.
order_pizza = PizzaOrder(chef)
order_pasta = PastaOrder(chef)

#Waiter needs to exist in real life
waiter = Waiter()
waiter.take_Order(order_pizza)
# Pizza Order Placed...
# Chef is cooking pizza

waiter.take_Order(order_pasta)
# Pasta Order Placed...
# Chef is cooking pasta

#This is how Command Pattern Works