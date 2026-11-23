class Logger:
    # class variable
    __instance = None   # We set instance zero here
    file_name: str
    log_count = 0

    def __new__(cls, file_name : str):  #This is an inbuilt method that we're overriding, job = creating new objects of a class.
        if cls.__instance == None:  
            cls.__instance = super().__new__(cls)   
            # This super() calls the python's inbuilt __new__ method that we're inheriting.. 
            # this above line creates new object for us.
            cls.__instance.file_name = file_name
            cls.__instance.log_count = 0
            return cls.__instance   # returns the 1st instance / object here.
        else:
            return cls.__instance   #keep returning the same instance / object everytime __new__ is called internally.

    def log(self,msg : str):
        print(f"Logging {msg} in {self.file_name}")
        self.log_count += 1         #Incrementing count with every new log entry.

    def get_log_count(self) -> int:
        return self.log_count

log1 = Logger("app.log")
log1.log("Hey")
# Logging Hey in app.log

log2 = Logger("app.log")
log2.log("Bye")
# Logging Bye in app.log

log3 = Logger("app.log")
log3.log("Good")
# Logging Good in app.log

print(log1.get_log_count())
print(log2.get_log_count())
print(log3.get_log_count())

# 3
# 3
# 3

print(id(log1), id(log2), id(log3))
# 1759736138448 1759736138448 1759736138448 same log object id here. Success.

"""
While creating objects - 

First Python runs the __new__(cls) to create and return new object 
Then Python runs the __init__(self) to initialise the object attributes passed by __new__

When to Use "__new__" ? 
    You override __new__ when you need to control object creation, such as:
        Subclassing immutable types (e.g., str, tuple, int)
        Implementing singleton or flyweight patterns
        Returning a different object type than the class being instantiated

When to Use "__init__" ?
    Use __init__ for normal initialization tasks:
        Setting attributes
        Preparing the object's state
        Running setup logic

"""