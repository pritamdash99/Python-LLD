class Airplane:
    def __init__(self, flight_number : str) -> None:
        self.__flight_number = flight_number

    def get_flight_number(self) -> str:
        return self.__flight_number

    def send_message(self, message: str, airplane : Airplane):
        print(f"{self.__flight_number} is sending {message} to {airplane.get_flight_number()}")

spicejet = Airplane("Spice-10ASD3")
indigo = Airplane("IN-2239D0")
airindia = Airplane("AIR-98SS34")

spicejet.send_message("(ETA - 5 Mins)",indigo)
spicejet.send_message("(ETA - 5 Mins)",airindia)
# Spice-10ASD3 is sending (ETA - 5 Mins) to IN-2239D0
# Spice-10ASD3 is sending (ETA - 5 Mins) to AIR-98SS34

indigo.send_message("(Got it Spicejet)",spicejet)
airindia.send_message("(Sure Spicejet)",spicejet)
# IN-2239D0 is sending (Got it Spicejet) to Spice-10ASD3
# AIR-98SS34 is sending (Sure Spicejet) to Spice-10ASD3

"""
ISSUES - 

There's a lot of 1-1 communication initiation being done from every airline for same message - Too Messy
All the airlines must have every other airlines' details.

Solution - 
Introduce a mediator -
1 airplane sends message to mediator then all the mediator sends same message to all other airplanes.
Basically broadcast should not be done 1 on 1.

We start by creating an interface AirTrafficControl
2 abstract methods - register_airplane() and send_message()

We create a concrete class - Control Tower inheriting the interface. 
We create a list of airplanes, the register_airplane would just append to that list for every new airplane.
For sendMessagage(Airplane), the sender Airplane will simply send messages to remaining airplanes using it's receieveMessage()

For Airplane class, we'll have a flight_number and Control Tower object in constructor.
Inside the sendMessage() of Airplane, it will just call the ControlTower's sendmessage(A).
1 more fucnction would be required - receiveMessage()
"""
