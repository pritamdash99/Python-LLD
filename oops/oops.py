#Object Oriented Programming
#Before OOP, ecode was written as a long list of instructions. 
#As projects grew bigger, it become messy and hard to manage. OOP solves this by organizing code around real-world objects.
#Everything in the real world is an object - OOP brings that thinking into code.
#Code is organized into classes, making it clean and structured.
#Easier to debug, extend and maintain large applications
#Built on 4 Pillars - Encapsulation, Inheritance, Polymorphism, Abstraction

# CLASSES AND OBJECTS 
# A class is just a template. Class = Blueprint ( eg. a design plan for a house)
# It doesn't hold any real data on it's own. 
# When you create an object from a class, that's when actual data gets stored and actions can be performed. 
# 
# Object = Actual instance built from that blueprint (eg. THE REAL HOUSE)
# A class defines what AATRIBUTES [ Data ] and METHODS [ Actions ] an object will have.
# Multiple objects can be created from the same class, each with their own data. 
# Ex - "Car" is a class. Your Honda City and Your Friend's Swift are 2 Different Objects.

# We start with bad examples of code and we keep getting better with more examples down below. 

class Student:
    name = ""
    age = 0 
    gender = ""

s1 = Student()
print(s1)
# O/p - <__main__.Student object at 0x0000019E95518980>
# you can fetch data or attributes of the object using dot operator.
print(s1.name)
print(s1.age)
print(s1.gender)
# O/p - Blank 0 Blank , They are empty because we haven't assigned any values to the attributes yet.
# So we need to set values.

s1.name = "Pritam"
s1.age = 27
s1.gender = "Male"
print(s1.name,s1.age,s1.gender)
# O/p - Pritam 27 Male

s2 = Student()
print(s2.name,s2.age,s2.gender) #Here we're printing individual attributes of s2 object.

# o/p - Blank 0 Blank , They are empty because we haven't assigned any values to the attributes yet.

# This also means that s2 doesn't have access to s1's data. Each object has its own data.

#EVERYTHING UP UNTIL NOW IS BAD CODE. NO OOP PRINCIPLES HAVE BEEN FOLLOWED.

class New_Student:
   # All the variables inside a class are called ATTRIBUTES. They are used to store data about the object.
    name = ""
    age = 0
    gender = ""

    #Functions inside a class are called METHODS. They are used to perform actions on the object.
    #It is compulsory to write "self" as the first parameter of a method. It is a reference to the current object.
    def display(self):
        print(f"This is a Display Method for {self}")

    def display_data(self):
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

ns1 = New_Student()
ns1.name = "Pritam"
ns1.age = 27
ns1.gender = "Male"
ns1.display()
# This is a Display Method for <__main__.New_Student object at 0x00000247E9DD8AD0>
ns1.display_data()
# My name is Pritam, age is 27 and gender is Male

ns2 = New_Student()
ns2.display()
#  This is a Display Method for <__main__.New_Student object at 0x0000022F8A0887D0>
ns2.display_data()
# My name is , age is 0 and gender is 

# With this new class, we optimised things by printing a function instead of printing each attribute individually.

# Another Problem - Every time we create a new object, we have to set the values of the attributes manually. 
# This is not efficient, we can solve it by creating a new method.



