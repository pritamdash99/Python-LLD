from abc import ABC, abstractmethod

class AirTrafficControl(ABC):
    @abstractmethod
    def register_plane(self, newAirplane : Airplane): pass

    @abstractmethod
    def sendMessage(self, message : str, to_airplane : Airplane): pass

class ControlTower(AirTrafficControl):
    def __init__(self) -> None:
        self.__airplanes : list[Airplane] = []

    def register_plane(self, newAirplane : Airplane):
        self.__airplanes.append(newAirplane)
        
    def sendMessage(self, message : str, to_airplane : Airplane):
        for airplane in self.__airplanes:
            if airplane != to_airplane:
                airplane.receiveMessage(message,to_airplane)

class Airplane:
    def __init__(self, flight_Number : str, tower : ControlTower) -> None:
        self.__flightNumber = flight_Number
        self.__tower = tower

        #Now we register the plane in the tower- 
        self.__tower.register_plane(self)

    def airplane_sendMessage(self, message : str):
        self.__tower.sendMessage(message,self)

    def get_flight_Number(self) -> str:
        return self.__flightNumber

    def receiveMessage(self, msg : str, sender : Airplane):
        print(f"{self.__flightNumber} got ({msg}) from {sender.get_flight_Number()}") 

# We start by creating our control Tower
controlTower = ControlTower()
airIndia = Airplane("AIR-565",controlTower)
spiceJet = Airplane("SPI-101",controlTower)
indigo = Airplane("IND-123",controlTower)

airIndia.airplane_sendMessage("On Runway")
# SPI-101 got (On Runway) from AIR-565
# IND-123 got (On Runway) from AIR-565

express = Airplane("EXP-676",controlTower)
express.airplane_sendMessage("TakeOff in 5 Mins")
# AIR-565 got (TakeOff in 5 Mins) from EXP-676
# SPI-101 got (TakeOff in 5 Mins) from EXP-676
# IND-123 got (TakeOff in 5 Mins) from EXP-676

#Now we don't need to make changes in any core classes, just create a Airplane Method & send message.