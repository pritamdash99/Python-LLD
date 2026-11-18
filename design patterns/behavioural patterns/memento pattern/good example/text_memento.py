class TextMemento:
    def __init__(self, text):   #This TMemento Object now gets used by History Class's Stack
        self.__saved_text = text 

    #getter for private attribute
    def get_text(self):
        return self.__saved_text
    