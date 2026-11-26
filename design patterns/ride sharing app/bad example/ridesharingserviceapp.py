from driver import Driver
from passenger import Passenger
from location import Location
from math import sqrt
from vehicle import Vehicle

class RidesharingServiceApp:
    def __init__(self) -> None:
        #when the object is created, by default we'll have a blank list of drivers and passengers
        self.drivers : list[Driver] = []
        self.passengers : list [Passenger] = []

    #method to add drivers
    def add_driver(self, driver : Driver):
        self.drivers.append(driver)

    #method to add passengers
    def add_passenger(self, passenger : Passenger):
        self.passengers.append(passenger)

    def checkDriverAvailability(self, drivers : list[Driver]) -> bool:
        # any(iterable) returns True if at least one element's bool in the iterable is True.
        return any(driver.available for driver in drivers)
        
    #method to book a ride
    # usually we take the location directly if we use google maps / maps api, from x1y1 to x2y2 and calculate distance then cost
    # for simplicity let's just ask the distance directly.
    def book_ride(self, passenger : Passenger, distance : float):
        #edge case 
        if len(self.drivers) == 0 or self.checkDriverAvailability(self.drivers) == False:
            print(f"No Drivers Available for Pickup for {passenger.name}")
            return

        # Hardcoded logic for assigning the passenger's nearest driver
        # We donot get into the calculation algorithm much for now - dfs, bfs, a lot of algo gets used. 
        assignedDriver = None
        minimumDistance = float("inf")
        for driver in self.drivers:
            if driver.available == True:
                # we find each driver's distance from the passenger
                currentDriverDistance = self.__calculate_distance(passenger.location, driver.location)
                if currentDriverDistance < minimumDistance:
                    # As the current driver is the closest to passenger
                    minimumDistance = currentDriverDistance
                    assignedDriver = driver
        
        if assignedDriver is None:
            return
        assignedDriver.available = False
        
        # Fare Calculation - would depend on vehicle type (maybe bike, maybe luxury car) and distance to travel
        expectedFare : float = self.__calculate_fare(assignedDriver.vehicle,distance)
        # Show the driver and fare to the passenger
        print(f"Ride Booked For {passenger.name} with {assignedDriver.name} with fare Rs.{expectedFare}")
        print(f"Driver is on the way and is {minimumDistance:.2f} away")

    def __calculate_distance(self, passenger_location : Location, driver_location : Location):
        #euclidean distance for simple distance calculation
        delta_x : float = passenger_location.get_latitude() - driver_location.get_latitude()
        delta_y : float = passenger_location.get_longitude() - driver_location.get_longitude()
        return sqrt(delta_x*delta_x + delta_y*delta_y)

    def __calculate_fare(self, vehicle : Vehicle, distance : float):
        if vehicle.type == "Car":
            return distance * 20    #Just hardcoded logic for distance * price per distance
        elif vehicle.type == "Bike":
            return distance * 10
        else:
            return distance * 8     # Default Rs.8 

