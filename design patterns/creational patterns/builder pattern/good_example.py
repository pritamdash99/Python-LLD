from abc import ABC, abstractmethod

#We first set things up with default value
class Laptop:
    processor: str | None = None
    ram : str | None = None
    graphicCard : str | None = None
    color : str | None = None
    screenSize : str | None = None

    def displaySpecs(self):
        print(f"Laptop Details\n\
        Processor = {self.processor}\n\
        Ram = {self.ram} GB\n\
        Graphics Card = {self.graphicCard}\n\
        Color = {self.color}\n\
        Screen Size = {self.screenSize} inch"
        )

#Using another builder class we set new values.
class LaptopBuilder:
    def __init__(self) -> None:
        #When we initialise a new Builder object, we'll a have a default Laptop set inside constructor
        self.__laptop = Laptop()

    def set_processor(self, processor: str):    #We set the values individually & return the same object.
        self.__laptop.processor = processor
        return self

    def set_ram(self, ram: str):
        self.__laptop.ram = ram
        return self 
    # If we don't return the same object then method chaining not possible as default return value = None

    def set_graphicCard(self, graphicCard: str):
        self.__laptop.graphicCard = graphicCard
        return self

    def set_color(self, color: str):
        self.__laptop.color = color
        return self

    def set_screenSize(self, screenSize : str):
        self.__laptop.screenSize = screenSize
        return self

    def build(self):
        return self.__laptop

# calling LaptopBuilder() directly gives us a LaptopBuilder object which will have a Laptop() object.
# .set_processor() returns (self) an object with processor set so on that specific object, we can call another method
# LaptopBuilder().set_process().set_ram().set... will thus keep setting values to the same object.
# This is known as method chaining.

lb1 = LaptopBuilder().set_processor("i7").set_ram("16")\
    .set_graphicCard("Nvidia").set_color("Red").set_screenSize("14")\
        .build()

print(lb1) # It returns a laptop object
# <__main__.Laptop object at 0x000001E645288AD0> 

lb1.displaySpecs()
"""
Laptop Details
        Processor = i7
        Ram = 16 GB
        Graphics Card = Nvidia
        Color = Red
        Screen Size = 14 inch
"""
print("===========\n")
lb2 = LaptopBuilder().set_ram("16").set_screenSize("14").build()
lb2.displaySpecs()
"""
Laptop Details
        Processor = None
        Ram = 16 GB
        Graphics Card = None
        Color = None
        Screen Size = 14 inch
"""