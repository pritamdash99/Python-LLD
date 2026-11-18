from text_memento import TextMemento
class TextEditor:
    def __init__(self) -> None:
        self.__text = ""

    def write(self, new_text) -> None:
        self.__text += new_text

    def get_text(self) -> str:
        return self.__text

    def save_text(self) -> TextMemento:
        return TextMemento(self.__text)