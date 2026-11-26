class UserService:
    def login(self, username : str, password : str) -> dict:
        print(f"[UserService] Logging in : {username}")
        return {"user_id" : "U123", "name" : username}

    def get_profile(self, user_id : str) -> dict:
        print(f"[UserService] Getting profile for : {user_id}")
        return {"user_id" : user_id, "name" : "Rahul", "address" : "Mumbai"}

class OrderService:
    def get_orders(self, user_id : str) -> list:
        print(f"[OrderService] Getting orders for : {user_id}")
        return [
            {"order_id" : "ORD-1", "total":1500},
            {"order_id" : "ORD-2", "total":3000},
        ]

#Client code - 
userService = UserService()
orderService = OrderService()

userService.login("uid","pwd1")
userService.get_profile("uid")
print(orderService.get_orders("uid"))

"""
[UserService] Logging in : uid
[UserService] Getting profile for : uid
[OrderService] Getting orders for : uid
[{'order_id': 'ORD-1', 'total': 1500}, {'order_id': 'ORD-2', 'total': 3000}]
"""

"""
ISSUE - 
Tight Coupling - here client must know what all service by UserService, but in reality it's kept hidden.
If get_profile inside UserSevice becomes get_profileee, then while creating object, client also must make it get_profileee. 
"""