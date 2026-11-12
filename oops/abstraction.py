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
"""