#This is the main file used for execution. 

from history import History
from text_editor import TextEditor
from text_memento import TextMemento

text_editor = TextEditor()
history = History()

text_editor.write("Hello")
text_editor.write(" World")
print(text_editor.get_text())
# Hello World

current_editor_state = text_editor.save_text() #This now becomes a memento object
history.save_state(current_editor_state) #This appends the current state into history list

text_editor.write(" Good")
text_editor.write(" Morning")

# We can directly add the text_editor.save_text() as an argument as it returns a memento
history.save_state(text_editor.save_text())

history.get_history_list()
# 0 Hello World
# 1 Hello World Good Morning

