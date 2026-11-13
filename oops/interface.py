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

