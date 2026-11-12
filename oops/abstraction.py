"""
ABSTRACTION - 

Abstraction is about reducing complexity.
You expose only the necessary details to the user and hide all the complicated internal logic. 
The user doesn't need to know how things work inside, just that they work.

Real life example - 
If there's an abstract class "Shape" which has 2 methods - area() and perimeter()
every class such as "Circle" or "Rectangle" that inherits "Shape" 
must without fail create both abstract methods for themselves.

If those 2 shape classes fail to create their versions of area() and perimeter() - Error Occurs
Also, the parent class Shape cannot have an object / instance, all operations must be carried out by the child classes.
That's why it's called "Abstract Class", A class with no object of it's own, just useful children.

And the child classes inheriting the Abstract Class = Concrete Classes
"""
#You'll need to import this module
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass #As I don't have anything to perform here.

    @abstractmethod
    def perimeter(self):
        pass

#s = Shape()
#print(s)
# TypeError: Can't instantiate abstract class Shape without an implementation for abstract methods 'area', 'perimeter'

#----------------------
# Let's start by creating a Rectangle but only implementing 1 method area()
class Rectangle(Shape):

    def __init__(self, length: int, breadth: int) -> None:
        self.length = length
        self.breadth = breadth

    def area(self) -> None:
        print(self.length * self.breadth)

rect = Rectangle(5,2) #Python didn't even let me create this Object
rect.area()
#TypeError: Can't instantiate abstract class Rectangle without an implementation for abstract method 'perimeter'

# EVERY CLASS INHERTING AN ABSTRACT CLASS = CONCRETE CLASS

