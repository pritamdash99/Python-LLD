#The middle interface that connects the Higher Level Module with Low Level Modules
from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message:str): pass
