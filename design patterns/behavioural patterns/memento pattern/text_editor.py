"""
This will be bad code example
The basic idea is - 
    If I write something in a text editor, it should get saved, 
    If I want to add another text then it should get added to the text
    If I want to undo my changes, it should get reflected on the text editor.
"""
class TextEditor:
    def __init__(self) -> None:
        self.__text = ""

    def write(self, new_text) -> None:
        self.__text += new_text

    def get_text(self) -> str:
        return self.__text

text_editor = TextEditor()
text_editor.write("My Name Is")
text_editor.write(" Pritam")
print(text_editor.get_text())
# My Name Is Pritam

"""
If there was an undo function - 
and if you said text_editor.undo() after the .write("Pritam")
and then if you did .get_text() it would have returned "My Name Is" and not "My Name Is Pritam"

It's obvious that a DS such as Stack could help us implement this functionality.
We would need to pop the last saved element in a stack incase of undo()
But all these functionalities should not be done in 1 class "text_editor", 
It violates (Single Responsibility Principle).

How do we implement this? 
Done in Good Example...
"""
