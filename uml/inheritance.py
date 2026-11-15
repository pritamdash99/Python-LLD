#Parent class (Superclass)
class Animal:
    def __init__(self,name: str, age:int) -> None:
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def eat(self) -> None:
        print(f"{self.__name} is eating...")

    def sleep(self) -> None:
        print(f"{self.__name} is sleeping...")

class Dog(Animal):  # Dog [IS - A] Animal
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)
        self.__breed = breed

    def get_breed(self) -> str:
        return self.__breed

    def bark(self) -> None:
        print(f"{self.get_name()} is barking...")

    def fetch(self) -> None:
        print(f"{self.get_name()} is fetching me ball...")

animal1 : Animal = Animal("Generic Animal",4)
animal1.eat()
animal1.sleep()
# Generic Animal is eating...
# Generic Animal is sleeping...

print("\n"+ "=" * 50 + "\n")

dog1 : Dog = Dog("Max", 3, "Golden Retriever")

dog1.eat()
dog1.sleep()
# Max is eating...
# Max is sleeping...

#Dog's own methods - 
dog1.bark()
dog1.fetch()
# Max is barking...
# Max is fetching me ball...