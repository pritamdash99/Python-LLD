# No object will be created for this class so Abstract Class
from abc import ABC, abstractmethod
from vehicle import Vehicle

class FareStrategy(ABC):
    @abstractmethod
    def calculateFare(self, vehicle : Vehicle, distance : float) -> float : pass

# Instead of hardcoding, we calculate fare at runtime.
class Standard_FareStrategy(FareStrategy):
    def calculateFare(self, vehicle: Vehicle, distance: float) -> float:
        return vehicle.get_fare_amount() * distance

class Shared_FareStrategy(FareStrategy):
    def calculateFare(self, vehicle: Vehicle, distance: float) -> float:
        return vehicle.get_fare_amount() * distance * 0.5

class Luxury_FareStrategy(FareStrategy):
    def calculateFare(self, vehicle: Vehicle, distance: float) -> float:
        return vehicle.get_fare_amount() * distance * 1.5