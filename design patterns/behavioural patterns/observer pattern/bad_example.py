#This is the execution without observer pattern
#We want to display Weather Degree changes on multiple devices.

class PhoneDisplay:
    def update(self, new_temp):
        print(f"Phone Display Temperature = {new_temp}")

class WeatherStation:
    def __init__(self) -> None:
        self.__temperature = 0 
        self.__phone_display = PhoneDisplay()

    def update_temperature(self, new_temp):
        self.__temperature = new_temp
        self.notify_display()

    def notify_display(self):
        self.__phone_display.update(self.__temperature)

ws = WeatherStation()
ws.update_temperature(25)
# Phone Display Temperature = 25
"""
For now, it seems to be working, what if we need more Display Devices? 
    You might consider adding more device classes and creating objects inside WS constructor.
    Then adding "self.tv_display.update(self.__temperature)" inside update_temperature().

You're changing the core Weather Station class again and again. BAD EXAMPLE.
"""
