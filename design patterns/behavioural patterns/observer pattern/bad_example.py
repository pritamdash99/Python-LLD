#This is the execution without observer pattern

class PhoneDisplay:
    def update(self, new_temp):
        print(f"Phone Display Temperature = {new_temp}")

class WeatherStation:
    def __init__(self) -> None:
        self.__temperature = 0 
        self.__phone_display = PhoneDisplay()

    def update_temperature(self, new_temp):
        self.__temperature = new_temp

    def 