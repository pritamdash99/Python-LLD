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
#ABC = Abstract Base Classes
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
"""
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

"""
#--------------------------------

class Rectangle(Shape):

    def __init__(self, length: int, breadth: int) -> None:
        self.length = length
        self.breadth = breadth

    def area(self) -> None:
        print(self.length * self.breadth)

    def perimeter(self) -> None:
        print(2 * (self.length + self.breadth))

rect = Rectangle(5,2) 
print("Rectangle Details - ")
rect.area()
rect.perimeter()
# Rectangle Details - 
# 10
# 14

class Circle(Shape):

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def area(self) -> None:
        print(2 * 3.14 * self.radius)

    def perimeter(self) -> None:
        print(self.radius ** 2)

circle = Circle(5)
print("Circle Details - ")
circle.area()
circle.perimeter()
# Circle Details - 
# 31.400000000000002
# 25

"""
ABSTRACTION VS INTERFACE

In Python, an INTERFACE is a blueprint or contract that defines a set of methods and properties a class 
    MUST implement, without providing the actual code for how those methods work.

Unlike languages such as Java or C#, Python does not have a dedicated "interface" keyword.
Instead developers use built-in language features to create and enforce interfaces.

Abstraction is a broad concept that hides complex details and shows only the essentials, 
whereas an interface is a specific tool used to achieve abstraction by 
defining a STRICT CONTRACT OF METHODS a class MUST follow.

Ex - 
Think of a car. 
ABSTRACTION is the dashboard - it hides the complex engine mechanics and 
    gives you simple controls like a steering wheel and pedals.
An INTERFACE is the universal rulebook that states -
every car MUST have a steering wheel, brake pedal and gas pedal so any driver can operate it. 

WHEN TO USE WHAT? 
    Use an Abstract Class (Abstraction) when classes are closely related (like Dog, Cat) 
        and you want to AVOID REPEATING SHARED CODE
    
    Use an Interface when unrelated classes (like Bird and Airplane) 
        need to support the same action without sharing a family tree.

Some More Examples - 
"""