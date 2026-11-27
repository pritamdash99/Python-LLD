#Here we create all objects and test logic

from location import Location
from vehicle import Vehicle
from ridematchingservice import RideMatchingService
from driver import Driver
from passenger import Passenger
from car import Car
from bike import Bike
from fare_strategy import Luxury_FareStrategy

loc1 = Location(15.3243, 81.2312)
loc2 = Location(16.6541, 82.8242)
loc3 = Location(15.9812, 82.8483)

car = Car("CS9999")
bike = Bike("PQ4211")

driver1 = Driver("Alice","alice@mail.com", loc2, car)
#driver2 = Driver("Bob","bob@mail.com",loc3, bike)

passenger1 = Passenger("Pritam", "pritam@mail.com",loc2)

rideMatchingService = RideMatchingService()
rideMatchingService.add_driver(driver1)
rideMatchingService.requestRide(passenger1,50,Luxury_FareStrategy())
"""
Notify To Passenger Pritam = Ride Scheduled with fare Rs.1500.0
Notify To Driver Alice = You have won new ride for Rs.1500.0
Notify To Driver Alice = Your ride is ONGOING
Notify To Passenger Pritam = Ride Status is ONGOING
Notify To Driver Alice = Your ride is COMPLETED
Notify To Passenger Pritam = Ride Status is COMPLETED
"""