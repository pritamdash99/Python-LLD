from abc import ABC, abstractmethod

class Employee(ABC) : 
    @abstractmethod
    def eat(self): pass

    @abstractmethod
    def work(self): pass

class Worker(Employee):
    def eat(self):
        print("Worker is eating")
    def work(self):
        print("Worker is working")

# Let's say I own a robotics company and have robot workers

class Robot(Employee):
    def work(self):
        print("Robot is working")

    def eat(self): #We are forcing a robot to eat even though it doesn't normally eat.
        raise Exception("Robot can't eat")
    #This violates ISP

r = Robot()
# Handling raised exception without crashing code.
try:
    r.eat()
except Exception as e:
    print("Exception found", e)
# Exception: Robot can't eat
