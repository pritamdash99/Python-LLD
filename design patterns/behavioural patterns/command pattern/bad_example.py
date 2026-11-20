class Chef:
    def cook_pizza(self):
        print("Chef is cooking pizza")

    def cook_pasta(self):
        print("Chef is cooking pasta")

class Waiter:
    #The waiter will know it's chef and it's abilities so we assign chef at initiation
    def __init__(self, chef : Chef) -> None:
        self.__chef = chef

    def place_order(self, item : str):
        if item == "pasta":
            self.__chef.cook_pasta()
        elif item == "pizza":
            self.__chef.cook_pizza()
        else:
            print("Cannot take order")

chef = Chef()
waiter = Waiter(chef)

waiter.place_order("pasta")
# Chef is cooking pasta

# seems to be working fine for now, but if chef decides to add " cook_biryani", 
# Waiter will need to add another elif item == "biryani". 
# Such tight coupling violets Open Closed Principle

"""
So, what to do now? How do we make this a loose couple? 

In real life, waiter doesn't need to know the details of chef's abilities.
Waiter's job is to take order bring food.

So, we create an Interface "Order" which will have an abstract method "execute"
And different type of orders such as "Burger Order", "Pizza Order" 
    will inherit the interface and call chef's cook_dish() in their own version of execute().
So, while initialising all the order types we'll take a Chef instance as parameter.

Inside the Waiter Class we'll have a method "take_order(Order)" which calls the respective order.execute()
Now all the waiter needs to do is - take the order & execute task.
"""
