"""
POLYMORPHISM - 

Poly means MANY, morph means FORMS.
Polymorphism allows the same method name to behave differently depending on which object calls it.
This makes your code highly flexible and extensible.

- same method name works differently for different classes
- you don't need to remember multiple method names for similar actions
- Method Overriding : Child class provides it's own version of a parent's method

Real life example : 
A "draw()" method 
on a Circle draws a circle, 
on a Rectangle draws a rectangle.
Same name method but different behavior.
"""
class Animal:
    def __init__(self, name: str, age: int) -> None:
        print("This is animal init")
        self.name = name
        self.age = age

    def eat(self) -> None:
        print("This animal is eating")

    def sleep(self) -> None:
        print("This animal is sleeping")

    def move(self) -> None:
        print("This animal is moving")

class Dog(Animal):
    def __init__(self, name:str, age:int, breed :str) -> None:
        super().__init__(name, age)
        self.breed = breed

    def bark(self) -> None:
        print("I am barking")

    def display(self) -> None:
        print(f"Dog's name is {self.name}, age is {self.age}, breed is {self.breed}")

    def move(self) -> None:
        print(f"{self.name} is moving")

dog1 = Dog("Max", 10, "German Shephard")
dog1.display()
dog1.move()

# This is animal init
# Dog's name is Max, age is 10, breed is German Shephard
# Max is moving

#So the dog class move() override the animal class move()