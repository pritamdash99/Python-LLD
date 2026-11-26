from location import Location
from vehicle import Vehicle
class Driver:
    def __init__(self, name: str, location : Location, vehicle : Vehicle) -> None:
        self.name = name
        self.location = location
        self.vehicle = vehicle
        self.available : bool = True   #To check if the driver is currently on a ride

    def get_location(self) -> Location:
        return self.location

    def set_location(self, location : Location) -> None:
        self.location = location
