# This class gets used for the undo operation implementation via a List of Memento Objects
from text_memento import TextMemento

class History:
    def __init__(self) -> None:
        self.__history : list[TextMemento]= [] #Starts with an empty list.

    def save_state(self, memento : TextMemento):
        self.__history.append(memento)

    def get_history_list(self):
        print(f"Curent history =")
        for i in range(len(self.__history)):
            print(f"{i} {self.__history[i].get_text()}")

    # UNDO Function
    def undo(self) -> TextMemento:
        if len(self.__history) > 0:
            self.__history.pop()    # pops the last saved memento
            if len(self.__history) == 0:
                return TextMemento("")  #if post popping no element present return blank text memento object
            return self.__history[-1] # post popping - returns the current last memento object in the list
        else:
            return TextMemento("") #if at starting no element present return blank text memento object