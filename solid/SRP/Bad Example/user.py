class User:
    def __init__(self, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email

    def get_user_info(self) ->None:
        print(f"This is {self.name} and my age is {self.age}")

    def is_adult(self) -> bool:
        return self.age > 18

    def save_to_database(self):
        print(f"{self.name} is getting saved to Database")

    def delete_user_from_database(self):
        print(f"{self.name} is getting deleted from Database")

# save_to_database() and delete_user_from_database() should not be this 1 class.
# It will work for now but when it'll be time to scale it will be headache.
