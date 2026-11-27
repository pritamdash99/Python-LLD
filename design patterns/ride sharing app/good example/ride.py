# We'll encapsulate all the ride details inside this file to make things easy
# Driver, Passenger, Fare strategy, Ride Status
from enum import Enum
from passenger import Passenger
from driver import Driver
from fare_strategy import FareStrategy

class RideStatus(Enum):
    SCHEDULED = "SCHEDULED"
    ONGOING = "ONGOING"
    COMPLETED = "COMPLETED"

class Ride:
    def __init__(
            self,
            passenger : Passenger,
            driver : Driver,
            distance : float,
            fare_strategy : FareStrategy
            ) -> None:

        self.passenger = passenger
        self.driver = driver
        self.distance = distance
        self.fare_strategy = fare_strategy
        self.fare : float = 0.0
        self.status : RideStatus = RideStatus.SCHEDULED

    def calculate_fare(self):
        self.fare = self.fare_strategy.calculateFare(self.driver.getVehicle(), self.distance)

    def getRideFare(self) -> float:
        return self.fare

    def updateStatus(self,new_ride_status : RideStatus):
        self.status = new_ride_status
        self.__notifyUsers(self.status)

    def __notifyUsers(self, status: RideStatus):
        self.driver.notify(f"Your ride is {status.value}")
        self.passenger.notify(f"Ride Status is {status.value}")

