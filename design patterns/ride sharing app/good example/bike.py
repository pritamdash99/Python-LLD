from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, number_plate: str) -> None:
        super().__init__(number_plate)

    def get_fare_amount(self) -> float:
        return 10 