"""
INHERITANCE - 

Inheritance allows one class to acquire the properties and methods of another class. 
This avoids writing the same code again and again, and makes your codebase much cleaner.

Parent Class (Also called BASE CLASS) - contains common, shared features. 
Child Class (Also called DERIVED CLASS) - inherits the features of the parent class.
Child class can also add it's own new attributes and methods on top. 
Changes made in the parent class automatically reflect in child classes.

Real life example - 
Animal class has eat() and sleep() methods. 
Dog and Cat class inherit these and Dog adds bark(), Cat adds meow() methods.
""" 
class Animal:
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.bark()
dog.eat()
dog.sleep()
# Dog is barking
# This animal is eating
# This animal is sleeping

animal = Animal()
animal.eat()
animal.sleep()
# This animal is eating
# This animal is sleeping

#--------------------------
#If all animals need name and age attributes, we can add them to the parent class.
class New_Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Cat(New_Animal):
    def meow(self):
        print("Cat is meowing")
    def display_info(self):
        print(f"Cat name is {self.name} and age is {self.age}")

Cat1 = Cat("Tom", 5) #Even though Cat class doesn't have init, it inherits the init method from New_Animal class.
Cat1.display_info()
#Cat name is Tom and age is 5
