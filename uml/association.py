class Student:
    def __init__(self, name: str) -> None:
        self.__name :str = name #Private

    def get_name(self) -> str:  #getter function
        return self.__name
    
class Teacher:
    def __init__(self, name:str) -> None:
        self.__name :str = name #Private

    def get_name(self) -> str:  #getter function
        return self.__name

    def teach(self, student: Student) -> None:    #association application
        print(f"{self.__name} is teaching {student.get_name()}")

teacher1 = Teacher("Panda Sir")
student1 = Student("Pritam")
teacher1.teach(student1)
# Panda Sir is teaching Pritam