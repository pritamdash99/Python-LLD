from user import User
from location import Location

class Passenger(User):
    #Calling super() will give us the necessary data but 1 more data - Vehicle Type
    def __init__(self, name: str, email: str, location: Location) -> None:
        super().__init__(name, email, location)
        