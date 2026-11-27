from driver import Driver
from passenger import Passenger
from location import Location
from fare_strategy import FareStrategy
from ride import Ride, RideStatus
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
        #Post finding nearestDriver, we remove it from our list as it'll be occupied with ride.
        if nearestDriver is not None:
            ride : Ride = Ride(passenger,nearestDriver,distance,strategy)
            ride.calculate_fare()
            passenger.notify(f"Ride Scheduled with fare Rs.{ride.getRideFare()}")
            nearestDriver.notify(f"You have won new ride for Rs.{ride.getRideFare()}")
            ride.updateStatus(RideStatus.ONGOING)

            #Upon Completion
            ride.updateStatus(RideStatus.COMPLETED)
            self.availableDrivers.append(nearestDriver)

    def findNearestDriver(self, passenger_location : Location) -> Driver | None:
        assignedDriver = None
        minimumDistance = float ("inf")
        for driver in self.availableDrivers:
            distance = driver.get_location().calculateDistance(passenger_location)
            if distance < minimumDistance:
                minimumDistance = distance
                assignedDriver = driver

        return assignedDriver