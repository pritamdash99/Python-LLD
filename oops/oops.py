"""
OBJECT ORIENTED PROGRAMMING - 
Before OOP, ecode was written as a long list of instructions. 
As projects grew bigger, it become messy and hard to manage. OOP solves this by organizing code around real-world objects.
Everything in the real world is an object - OOP brings that thinking into code.
Code is organized into classes, making it clean and structured.
Easier to debug, extend and maintain large applications
Built on 4 Pillars - Encapsulation, Inheritance, Polymorphism, Abstraction

CLASSES AND OBJECTS -
A class is just a template. Class = Blueprint ( eg. a design plan for a house)
It doesn't hold any real data on it's own. 
When you create an object from a class, that's when actual data gets stored and actions can be performed. 
 
Object = Actual instance built from that blueprint (eg. THE REAL HOUSE)
A class defines what AATRIBUTES [ Data ] and METHODS [ Actions ] an object will have.
Multiple objects can be created from the same class, each with their own data. 
Ex - "Car" is a class. Your Honda City and Your Friend's Swift are 2 Different Objects.

"""
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

class Another_Student:
    name = ""
    age = 0
    gender = ""
    def set_info(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")

    def display_data(self):
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

as1 = Another_Student()
#as1.set_info()
#as1.display_data()
# Enter Name: Pritam 
# Enter Age: 27
# Enter Gender: Male
# My name is Pritam, age is 27 and gender is Male

# The above code is much more organised and efficient. 
# We can create as many objects as we want and set their data using the set_info method.
# But this code can be optimised even further. We can pass the data as parameters to the set_info method instead of taking input from the user.

class Good_Student:
    name = ""
    age = 0
    gender = ""

    def set_info(self,name,age,gender):
        #self.name refers to the attribute of the object, but name refers to the parameter passed to the method.
        # All we're doing is assigning parameter values to the attributes of the object.

        self.name = name
        self.age = age
        self.gender = gender

    def display_data(self):
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

gs1 = Good_Student()
gs1.set_info("Pritam",27,"Male")
gs1.display_data()
#My name is Pritam, age is 27 and gender is Male

# Let's learn about ANOTATIONS. Annotations are a way to add metadata to your code. 
# Any new developer in your team can easily understand what type of data is expected in the parameters of a method.


class Annotation_Student:
    name = ""
    age = 0
    gender = ""

    def set_info(self,name :str,age :int,gender :str):
        #Python won't throw an error if you pass a different type of data to the method, but it will give a warning.
        #It's a good practice to use annotations to make your code more readable and maintainable.
        self.name = name
        self.age = age
        self.gender = gender

    def display_data(self):
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

gs1 = Annotation_Student()
gs1.set_info("Pritam",31,"Male")
gs1.display_data()
#My name is Pritam, age is 31 and gender is Male

# Process suggests to first set then display, but what if I don't set and directly display? 
# It will give blank values. Why does this happen? 
# Because the attributes are set to default values when the object is created.

# If we delete the 1st default values, then we get a "AttributeError: 'Annotation_Student' object has no attribute 'name'" error.
# So using the current way of code we are UPDATING the attributes of the object after it is created. 
# But instead of UPDATING we can directly set the attributes of the object when it is created.

class Set_Student:
    def set_info(self,name :str,age :int,gender :str):
        # Here we directly CREATE the attributes of the object when object is created. NO UPDATING.
        self.name = name
        self.age = age
        self.gender = gender

    def display_data(self):
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

ss1 = Set_Student()
ss1.set_info("Student 1",12,"Male")
ss1.display_data()
#My name is Student 1, age is 12 and gender is Male

# As humans, there is a possibility we might forget to SET the attributes of the object after it is created.
# This will always throw error when we try to display the data.
 
# What we need is a way to ask for data on the line the object is created.
# So we can solve this problem by using a special method called __init__(), aka INITIALIZER OR CONSTRUCTOR.

class Init_Student:
    def __init__(self,name :str,age :int,gender :str) -> None:
        # This method is automatically called when an object is created.
        # It is used to initialize the attributes of the object.
        print("This is an intializer / constructor")
        self.name = name
        self.age = age
        self.gender = gender

    def display_data(self) -> None:
        # Always a good practice to add return type to the method. Will help other developers.
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

    def get_age(self) -> int:
        return self.age

is1 = Init_Student("New",15,"Female")
is1.display_data()
# This is an intializer / constructor
# My name is New, age is 15 and gender is Female
is2 = Init_Student("Old",30,"Male")
print(is2.get_age())
# This is an intializer / constructor
# 30