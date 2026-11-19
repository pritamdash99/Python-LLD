from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update_temp(self, new_temp:int):
        pass