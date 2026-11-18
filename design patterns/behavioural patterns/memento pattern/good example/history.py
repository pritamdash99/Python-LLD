# This class gets used for the undo operation implementation via a List of Memento Objects
from text_memento import TextMemento

class History:
    def __init__(self) -> None:
        self.__history : list[TextMemento]= [] #Starts with an empty list.

    def save_state(self, memento : TextMemento):
        self.__history.append(memento)

    def get_history_list(self):
        print(f"Curent history = \n")
        for i in range(len(self.__history)):
            print(f"{i} {self.__history[i].get_text()}")

    