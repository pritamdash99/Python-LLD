# Most things are kept same, we just create an API Gateway in middle.

from abc import ABC, abstractmethod

class UserService:
    def login(self, username : str, password : str) -> dict:
        print(f"[UserService] Logging in : {username}")
        return {"user_id" : "U123", "name" : username}

    def get_profile(self, user_id : str) -> dict:
        print(f"[UserService] Getting profile for : {user_id}")
        return {"user_id" : user_id, "name" : "Pritam", "address" : "Bbsr"}

class OrderService:
    def get_orders(self, user_id : str) -> list:
        print(f"[OrderService] Getting orders for : {user_id}")
        return [
            {"order_id" : "ORD-1", "total":1500},
            {"order_id" : "ORD-2", "total":3000},
        ]

class APIGateway:
    def __init__(self) -> None:
        #We create instances of both Service Types and create respective methods inside Gateway.
        self.__user_service = UserService()
        self.__order_service = OrderService()

    def login_user(self, username : str, password : str):
        print(self.__user_service.login(username,password))

    def get_user_profile(self, userid : str): 
        print(self.__user_service.get_profile(userid))

    def get_order_details(self, userid : str):
        print(self.__order_service.get_orders(userid))

    def get_all_details(self, userid : str, userName : str, pwd : str):
        print(self.__user_service.login(userName,pwd))
        print(self.__user_service.get_profile(userid))
        print(self.__order_service.get_orders(userid))

api_gateway = APIGateway()

print("Client is making 3 separate API Calls")
api_gateway.login_user("Name1","Pwd1")
api_gateway.get_user_profile("Uid1")
api_gateway.get_order_details("Uid1")

print("\n--------------\nClient is making only 1 API Call")
api_gateway.get_all_details("NewID","newName","Password")

"""
Client is making 3 separate API Calls
[UserService] Logging in : Name1
{'user_id': 'U123', 'name': 'Name1'}
[UserService] Getting profile for : Uid1
{'user_id': 'Uid1', 'name': 'Pritam', 'address': 'Bbsr'}
[OrderService] Getting orders for : Uid1
[{'order_id': 'ORD-1', 'total': 1500}, {'order_id': 'ORD-2', 'total': 3000}]

--------------
Client is making only 1 API Call
[UserService] Logging in : newName
{'user_id': 'U123', 'name': 'newName'}
[UserService] Getting profile for : NewID
{'user_id': 'NewID', 'name': 'Pritam', 'address': 'Bbsr'}
[OrderService] Getting orders for : NewID
[{'order_id': 'ORD-1', 'total': 1500}, {'order_id': 'ORD-2', 'total': 3000}]

"""

"""
Thus client is no longer in touch with creating objects for internal classes and method calling.
Plus Client gets to make only 1 API call and access all the details.
"""