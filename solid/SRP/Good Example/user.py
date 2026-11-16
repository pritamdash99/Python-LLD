#Here we divide the tasks per class

class User:
    def __init__(self, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email

    def get_user_info(self) ->None:
        print(f"This is {self.name} and my age is {self.age}")

    def is_adult(self) -> bool:
        return self.age > 18

