from abc import ABC, abstractmethod

class SystemComponent (ABC):
    @abstractmethod
    def showdetails(self) : pass

class File(SystemComponent):
    def __init__(self, name : str) -> None:
        self.__name = name

    def showdetails(self):
        print(f"File : {self.__name}") 

class Folder(SystemComponent):
    def __init__(self, folder_name : str) -> None:
        self.__folderName = folder_name
        # We need a structure that can accept files and folders.
        self.__components : list[SystemComponent] = []

    def add_component(self, component : SystemComponent):
        self.__components.append(component)

    def showdetails(self):
        print(f"Folder Name : {self.__folderName}")
        for component in self.__components:
            component.showdetails()      #Recursion takes place to get inside nested folders.

file1 = File("image.png")
file2 = File("abc.ppt")
file3 = File("word.docx")

sub_folder = Folder("Drive")
sub_folder.add_component(file1)
sub_folder.add_component(file2)
sub_folder.add_component(file3)

image_file = File("Image 1.png")
movie = File("Heropanti.mov")

mainFolder = Folder("Main Folder")
mainFolder.add_component(image_file)    
mainFolder.add_component(movie)
mainFolder.add_component(sub_folder)    
# There's uniformity in .add_component(), file or folder, they get added.

mainFolder.showdetails()

"""
Folder Name : Main Folder
File : Image 1.png
File : Heropanti.mov
Folder Name : Drive
File : image.png
File : abc.ppt
File : word.docx
"""