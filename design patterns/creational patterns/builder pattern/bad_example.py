

class Laptop:       
    def __init__(self, 
                 processor : str, 
                 ram : str,                     # Permanent Variable
                 graphicCard : str | None = None,  #graphicCard is string / None with default value = None
                 color : str | None = None,     # All None Value arguments = Optional Variables.
                 screenSize : str | None = None
                 ) -> None:

        self.processor = processor
        self.ram = ram
        self.graphicCard = graphicCard
        self.color = color
        self.screenSize = screenSize

    def displaySpecs(self):
        print(f"Laptop Details\n\
Processor = {self.processor}\n\
Ram = {self.ram} GB\n\
Graphics Card = {self.graphicCard}\n\
Color = {self.color}\n\
Screen Size = {self.screenSize}"
)

#----------------------
l1 = Laptop("i3","8")
l1.displaySpecs()
"""
Laptop Details
Processor = i3
Ram = 8 GB
Graphics Card = None
Color = None
Screen Size = None
"""

l2 = Laptop("i5","16",None,"Blue",None)
l2.displaySpecs()
"""
Laptop Details
Processor = i5
Ram = 16 GB
Graphics Card = None
Color = Blue
Screen Size = None
"""

# We can't really say which arguments we're passing None To! 
# At 15 argument requirements, it'll be difficult to track.

"""
Problem - 
When a class constructor has needs too many parameters ( especially optional ones ), the Builder Pattern lets you construct complex objects step by step in a clear and readable way.

Solution - 
Splits the object creation process into separate steps using a builder class.
You can set only the properties you need using a fluent interface ( method chaining ), 
    making the code clean and easy to understand.

"""