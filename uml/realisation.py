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