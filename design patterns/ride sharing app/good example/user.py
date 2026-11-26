# As both driver and passenger have names, emails, locations 
# And we won't need to create a User Object [Only Driver and Passenger Object]
# let's have a USER as abstract class.

from abc import ABC, abstractmethod
from location import Location

class User(ABC):
    def __init__(self, name : str, email : str, location : Location) -> None:
        self.name = name
        self.email = email
        self.location = location

    def get_location(self):
        return self.location

    def set_location(self, newlocation : Location):
        self.location = newlocation
