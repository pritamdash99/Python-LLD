class Airplane:
    def __init__(self, flight_number : str) -> None:
        self.__flight_number = flight_number

    def get_flight_number(self) -> str:
        return self.__flight_number

    def send_message(self, message: str, airplane : Airplane):
        print(f"{self.__flight_number} is sending {message} to {airplane.get_flight_number()}")


