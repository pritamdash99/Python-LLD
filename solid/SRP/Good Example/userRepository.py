from user import User
#We import the user class and use it's attributes.
#The current UserRepository will have a user Object inside it's User Repository Object.

class UserRepository:
    def __init__(self, db, user : User, password) -> None:
        self.db = db
        self.user = user
        self.password = password

    def save_to_database(self, user : User):
        print(f"{user.name} is getting saved to Database")

    def delete_user_from_database(self, user : User):
        print(f"{user.name} is getting deleted from Database")

# We test it in a different file (main.py)
# Combo of all 3 classes = clean code.
