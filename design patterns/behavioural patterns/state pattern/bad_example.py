#here we make use of enums for different transport types 

from enum import Enum

class TransportMode(Enum):
    WALKING = "walking"
    BIKE = "bike"
    TRAIN = "train"

class TransportService: #collects a transport mode and gives transport service
    def __init__(self, transport_mode  : TransportMode) -> None:
        self.__transportMode = transport_mode

    #To set a fresh mode
    def set_mode(self,new_transport_mode : TransportMode):
        self.__transportMode = new_transport_mode

    def eta(self): 
        #Heavy If - Else Implementation of ETA
        if self.__transportMode == TransportMode.WALKING:
            #eta logic for walking...
            print("Walking will take 50 mins")
        elif self.__transportMode == TransportMode.BIKE:
            #eta logic for Bike...
            print("Bike will take 20 mins")
        elif self.__transportMode == TransportMode.TRAIN:
            #eta logic for Train...
            print("Train will take 15 mins")

    def give_directions(self):
        #Heavy If - Else Implementation of ETA
        if self.__transportMode == TransportMode.WALKING:
            #direction logic for walking...
            print("Go straight and take left")
        elif self.__transportMode == TransportMode.BIKE:
            #direction logic for Bike...
            print("Up the flyover")
        elif self.__transportMode == TransportMode.TRAIN:
            #direction logic for Train...
            print("Be seated in your coach")

transportService = TransportService(TransportMode.WALKING)
transportService.eta()
transportService.give_directions()

# Walking will take 50 mins
# Go straight and take left

transportService.set_mode(TransportMode.BIKE)
transportService.eta()
transportService.give_directions()
# Bike will take 20 mins
# Up the flyover

"""


"""