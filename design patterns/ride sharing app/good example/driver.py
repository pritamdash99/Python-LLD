from user import User
from location import Location
from vehicle import Vehicle

class Driver(User):
    #Calling super() will give us the necessary data but 1 more data - Vehicle Type
    def __init__(self, name: str, email: str, location: Location, vehicle : Vehicle) -> None:
        super().__init__(name, email, location)
        self.__vehicle = vehicle

    def getVehicle(self) -> Vehicle:
        return self.__vehicle
    