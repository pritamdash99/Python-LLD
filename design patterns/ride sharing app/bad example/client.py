#Here we create all objects and test logic

from location import Location
from vehicle import Vehicle
from ridesharingserviceapp import RidesharingServiceApp
from driver import Driver
from passenger import Passenger

loc1 = Location(15.3243, 81.2312)
loc2 = Location(16.6541, 82.8242)
loc3 = Location(15.9812, 82.8483)

car = Vehicle("CS9999","Car")
bike = Vehicle("PQ4211","Bike")

driver1 = Driver("Alice", loc2, car)
driver2 = Driver("Bob", loc3, bike)

passenger1 = Passenger("Pritam", loc1)

rideservice = RidesharingServiceApp()
rideservice.add_driver(driver1)
rideservice.add_driver(driver2)
rideservice.add_passenger(passenger1)

rideservice.book_ride(passenger1,30)
# Ride Booked For Pritam with Bob with fare Rs.300        As P at loc1 and Bob at loc3, closer than loc2
# Driver is on the way and is 1.75 away

passenger2 = Passenger("Bhanu", loc2)
rideservice.add_passenger(passenger2)
rideservice.book_ride(passenger2,50)
# Ride Booked For Bhanu with Alice with fare Rs.1000       As both P and Alice are at loc2
# Driver is on the way and is 0.00 away

passenger3 = Passenger("Rocky", loc3)
rideservice.add_passenger(passenger3)
rideservice.book_ride(passenger3,10)
# No Drivers Available for Pickup for Rocky

"""
ISSUES - 
    (SRP)Single Responsibility Principle gets violated with RidesharingServiceApp class - 
        It manages the drivers & passengers repository.
        Bookride() is being managed here
        Fare Calculation is being managed here
    
    OCP is getting violated as - 
        Vehicle type is hard coded as string inside calculate fare
        Tomorrow if there's another type, it'll be added inside core ridesharing class
    
    LSP is getting violated as we're matching with string..
        vehicle.type == "Car"
        All these vehicles could have been an interface
        & later All new and old vehicle types could inherit the interface without core code change.

    DIP is getting violated as RideSharingSeviceApp is high level but it has calculatefare() which is a low level.
        Low level code updation should not affect the core high level code base.

"""