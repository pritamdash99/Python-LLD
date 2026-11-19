from observer import Observer

class Desktop_Display(Observer):
    def update_temp(self, new_temp: int):
        print(f"Desktop Temperature updated to {new_temp}")
