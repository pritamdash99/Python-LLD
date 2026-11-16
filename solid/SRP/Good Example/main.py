# We import respective classes
from user import User
from userRepository import UserRepository

#Here we create respective objects and implement the code
user_obj = User("Pritam", 27, "pd@gmail.com")
user_obj.get_user_info()

user_repo = UserRepository("DB",user_obj,"root")
user_repo.save_to_database(user_obj)

# This is Pritam and my age is 27
# Pritam is getting saved to Database