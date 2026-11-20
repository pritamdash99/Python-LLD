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
