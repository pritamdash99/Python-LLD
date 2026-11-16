# 1.  Use Abstract Base Class - Nominal Subtyping when you want run time enforcement.
# If a concrete class fails to implement every @abstractmethod, Python raises a Type Error at Objection creation

from abc import ABC, abstractmethod
#Interface
class Owner(ABC):
    @abstractmethod
    def acquire_ownership(self, property : str):
        pass

    @abstractmethod
    def dispose_ownership(self, property : str):
        pass

#Person Realises Owner
class Person(Owner):
    def acquire_ownership(self, property: str):
        print(f"Person acquired {property}")

    def dispose_ownership(self, property: str):
        print(f"Person disposed {property}")

#Corporation Realises Owner
class Corporation(Owner):
    def acquire_ownership(self, property):
        print(f"Corporation acquired {property}")

    def dispose_ownership(self, property: str):
        print(f"Corporation disposed {property}")

p = Person()
c = Corporation()

p.acquire_ownership("House")
p.dispose_ownership("House")
# Person acquired House
# Person disposed Houe

c.acquire_ownership("Hotel")
c.dispose_ownership("Hotel")
# Corporation acquired Hotel
# Corporation disposed Hotel

# ----------------------------------

# 2. Use typing.Protocol - Structural Subtyping
# Use protocol when you want clean, Pythonic static type checking without 
#   forcing classes to inherit from a common base class. 
# A class realises the protocol simply by defining the matching methods.

from typing import Protocol

# Define Protocol [contract]
class Notifier(Protocol):
    def send(self, message : str) -> None:
        pass

# Concrete classes realize the contract implicity [no inheritance needed]
class EmailNotifier:
    def send(self, message : str) -> None:
        print(f"Email sent - {message}")

class SMSNotifier:
    def send(self, message : str) -> None:
        print(f"SMS sent - {message}")

# static type checkers (mypy/Pyright/IDEs) verify realisation automatically
def alert_user(notifier: Notifier, text : str) -> None:
    notifier.send(text)

alert_user(EmailNotifier(), "Your Order has shipped")
alert_user(SMSNotifier(), "Your OTP is 482910")
# Email sent - Your Order has shipped
# SMS sent - Your OTP is 482910