class DiscountService:
    def calculate_discount(self, discount_type : str):
        if discount_type == "diwali":
            print("Applying diwali discount of 20%")
        elif discount_type == "first_order":
            print("Applying first order discount of 15%")
        else: 
            print("No Discount Applied")

ds = DiscountService()
ds.calculate_discount("diwali")
# Applying diwali discount of 20%

"""
Problems in code - Issues with the if-else approach : 
- Too many responsibilities : 
    The DiscountService class is doing 2 jobs. 
    Deciding which discount to apply AND calculating the discount. 
    It should only do 1 job (violates Single Responsibility Principle)
- Hard to extend : 
    Everytime you want to add a new discount type (Like Republic Day sale), you have to open the DiscountService class and add more if-else statements. 
    This means changing existing working code.
- Messy Code : 
    As you keep adding more discount types, the if-else chain becomes longer and longer, making the code harder to read, understand and maintain.

What could be done for it?
    As we know we'll need to assign different types of discount strategy - 
    We can have an Interface "DiscountStrategy" with abstract method - @calculate_discount
    And all different discount types can inherit this interface.

    Now we need a way to access and update the discount types in the main class.
    So we can create a basic Discount Strategy object inside DiscountService Class (default discount)
    Then to update future strategy we can have a setter method. 
    Then inside a function of Discount Service, we can call the ".calculate_discount()" 

    So in future, the main Discount Service class remains uninterrupted, we only make more discount types.
"""