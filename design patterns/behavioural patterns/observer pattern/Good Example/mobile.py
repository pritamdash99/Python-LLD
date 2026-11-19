from observer import Observer

class Mobile_Display(Observer):
    def update_temp(self, new_temp: int):
        print(f"Mobile Temperature updated to {new_temp}")
