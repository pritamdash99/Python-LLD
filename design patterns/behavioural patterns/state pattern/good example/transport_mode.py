#This will be our transport interface

from abc import ABC, abstractmethod

class TransportMode(ABC):

    @abstractmethod
    def eta(self): pass

    @abstractmethod
    def give_direction(self):pass
    