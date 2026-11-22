from abc import ABC, abstractmethod

class AirTrafficControl(ABC):
    @abstractmethod
    def register_plane(self, newAirplane : Airplane): pass

    @abstractmethod
    def sendMessage(self, message : str, airplane : Airplane): pass

class ControlTower(AirTrafficControl):
    def __init__(self) -> None:
        self.__airplanes : list[Airplane] = []

    def register_plane(self, newAirplane : Airplane):
        self.__airplanes.append(newAirplane)
        
    def sendMessage(self, message : str, airplane : Airplane):
        for airplane in self.__airplanes:
            airplane.receiveMessage(message,airplane)

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

