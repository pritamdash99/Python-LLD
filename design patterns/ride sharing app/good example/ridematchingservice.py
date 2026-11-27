from driver import Driver
from passenger import Passenger
from location import Location
from fare_strategy import FareStrategy
#We'll maintain single responsibility - 
class RideMatchingService:
    def __init__(self) -> None:
        self.availableDrivers : list [Driver] = []

    def add_driver(self, driver : Driver):
        self.availableDrivers.append(driver)

    def requestRide(self, passenger : Passenger, distance : float, strategy : FareStrategy):
        #Edge case 
        if len(self.availableDrivers) == 0: 
            passenger.notify("No Drivers Available")
            return
        #Nearest Driver
        nearestDriver : Driver | None = self.findNearestDriver(passenger.get_location())
        passenger.notify("Ride has been booked")

    def findNearestDriver(self, passenger_location : Location) -> Driver | None:
        assignedDriver = None
        minimumDistance = float ("inf")
        for driver in self.availableDrivers:
            distance = driver.get_location().calculateDistance(passenger_location)
            if distance < minimumDistance:
                minimumDistance = distance
                assignedDriver = driver

        return assignedDriver