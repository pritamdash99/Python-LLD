from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, number_plate: str) -> None:
        super().__init__(number_plate)

    def get_fare_amount(self) -> float:
        return 20
    
#car should show options - standard, shared, luxury

