from abc import ABC, abstractmethod

# We never actually create the object for Vehicle we create objects for Cars, Bikes
class Vehicle:
    def __init__(self, number_plate : str) -> None:
        self.numberPlate = number_plate

    @abstractmethod
    def get_fare_amount(self) -> float : pass