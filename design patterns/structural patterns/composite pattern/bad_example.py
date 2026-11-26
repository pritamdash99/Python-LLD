class File:
    def __init__(self, name : str) -> None:
        self.__name = name

    def show_details(self) -> str:
        return f"File : {self.__name}"

class Folder:
    def __init__(self, folder_name : str) -> None:
        self.__folderName = folder_name
        self.__files : list[File] = []

    def add_file(self, file : File):
        self.__files.append(file)

    def show_details(self):
        print(f"Folder Name : {self.__folderName}")
        for file in self.__files:
            print(file.show_details())

file1 = File("image.png")
file2 = File("abc.ppt")
file3 = File("word.docx")

folder = Folder("drive")
folder.show_details()
# Folder Name : drive

folder.add_file(file1)
folder.add_file(file2)
folder.add_file(file3)
folder.show_details()
"""
Folder Name : drive
File : image.png
File : abc.ppt
File : word.docx
"""

"""
ISSUES - 
    What if we want to add a folder inside a folder?
    We want to have a system that lets you have a nested folder -> folder -> file system.
"""