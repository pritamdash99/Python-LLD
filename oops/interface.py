"""
Definition covered in abstraction.py

Now we see 3 Types of interfaces available in Python.

1. Informal - "Please follow this rule, or the program might crash later."
2. Formal (ABC) - "You must inherit from me and folow this rule, or you aren't allowed to exist."
3. Protocol - "I don't care where you came from, as long as you have speak() button I can press."
"""

"""
1. INFORMAL INTERFACE [THE "HONOR SYSTEM"]

An informal interface is just a normal parent class. 
It sets a rule for child classes, but Python does not actually enforce it until you try to use the missing method.

-   You write a parent class with a placeholder method. 
    Child classes are expected to replace it with their own version.

-   But, if you forget to write that placeholder method in child class, Python lets you create the child class anyway.
    Your program will only crash later when you actually ask it to use unimplemented placeholder method.
"""

#The Interface [Rulebook]
class Animal:
    def speak(self):
        raise NotImplementedError("Every animal must speak!")

#Valid Child Class
class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

#Broken Child Class (Forget to add speak)
class Fish(Animal):
    pass

#Running the code:
dog = Dog()
print(dog.speak())

fish = Fish()
#Ran the code, no error until this part.

#print(fish.speak())
# Code crashed! 
# NotImplementedError: Every animal must speak!

"""
2. Formal Interface (abc.ABC - The "Strict Guard")

A formal interface uses Python's abc( Abstract Base Class) tool to 
    strictly enforce rules the exact moment you create an object.

- You inherit from ABC and put @abstractmethod above required methods.
    Child classes MUST inherit from this class and implement the method. 

- But, Python acts like a strict security guard. 
    If a child class is missing said methods, Python blocks you from creating the object at all.
"""

from abc import ABC, abstractmethod

#The interface - strict rulebook
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

#Valid Child Class
class Cat(Animal):
    def speak(self) -> str:
        return "Meow!!"

#Broken Child Class (Forgot to add speak)
class Snake(Animal):
    pass

#Run the code
cat = Cat()
print(cat.speak)    #Output :Meow! 

#snake = Snake() #Code CRASHED on this line.
# TypeError: Can't instantiate abstract class Snake without an implementation for abstract method 'speak'
