from transport_mode import TransportMode

class TransportService:
    def __init__(self, mode: TransportMode) -> None:
        self.__mode = mode

    #setter
    def set_mode(self, new_mode : TransportMode):
        self.__mode = new_mode

    #we need to be able to use the respective TransportMode's methods as Transport Service available by that mode
    def use_eta(self):
        self.__mode.eta()

    def use_directions(self):
        self.__mode.give_direction()

    #Now this transport service class need not be updated when a new transport mode is being added.
    #Thus Open Close Principle is maintained.