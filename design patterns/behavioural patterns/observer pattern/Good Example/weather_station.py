from observer import Observer

class WeatherStation:
    def __init__(self) -> None:
        self.__temperature : int = 0
        self.__observerList : list[Observer] = []

    def add_Observer(self, new_Observer : Observer):
        self.__observerList.append(new_Observer)

    def remove_Observer(self, observer : Observer):
        self.__observerList.remove(observer)

    def update_temperature(self, new_temp : int):
        self.__temperature = new_temp
        # Now we need to notify observers
        self.notify_Observers()

    def notify_Observers(self):
        for observer in self.__observerList:
            observer.update_temp(self.__temperature)