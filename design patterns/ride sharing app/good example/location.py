from math import sqrt

class Location:
    def __init__(self, latitude : float, longitude : float) -> None:
        self.__latitude = latitude
        self.__longitude = longitude

    def get_latitude(self) -> float:
        return self.__latitude

    def get_longitude(self) -> float:
        return self.__longitude

    #Distance calculation should be inside Location

    def calculateDistance(self, location : Location):
        delta_x : float = self.get_latitude() - location.get_latitude()
        delta_y : float = self.get_longitude() - location.get_longitude()
        return sqrt(delta_x*delta_x + delta_y*delta_y)
    # will be called as location1.calculteDistance(location2)

    