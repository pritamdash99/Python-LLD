from observer import Observer

class TV_Display(Observer):
    def update_temp(self, new_temp: int):
        print(f"TV Temperature updated to {new_temp}")
