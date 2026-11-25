import time

class HighResolutionImage:
    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name
        self.__image_data = None
        #Once image is initialised, we load the image from disk
        self._load_from_disk()

    def _load_from_disk(self):
        time.sleep(1)
        self.__image_data = f"[[Loaded image data of {self.__file_name}]]"
        print(f"Loaded {self.__file_name} from disk")

    def display_image(self):
        print(f"{self.__file_name} has image data of {self.__image_data}")

#We add a proxy class
class ImageProxy:
    def __init__(self, file_name : str) -> None:
        self.__file_name = file_name
        self.__real_image = None

    def display(self):
        if self.__real_image is None:   #If its is blank, only then an image gets created + loaded.
            self.__real_image = HighResolutionImage(self.__file_name)
        #If it isn't blank, meaning real_image is already created + loaded and ready to be displayed. 
        self.__real_image.display_image()

class PhotoGallery:
    def __init__(self) -> None:
        self.__images : list[ImageProxy] = []

    def add_image(self, filename: str):
        image_proxy = ImageProxy(filename)
        self.__images.append(image_proxy)

    def displayGallery(self):
        for image in self.__images:
            image.display()

gallery = PhotoGallery()
gallery.add_image("Image 1.png")
gallery.add_image("Image 2.png")
gallery.add_image("Image 3.png")
gallery.add_image("Image 4.png")
gallery.add_image("Image 5.png")

gallery.displayGallery()
"""
Loaded Image 1.png from disk
Image 1.png has image data of [[Loaded image data of Image 1.png]]
Loaded Image 2.png from disk
Image 2.png has image data of [[Loaded image data of Image 2.png]]
Loaded Image 3.png from disk
Image 3.png has image data of [[Loaded image data of Image 3.png]]
Loaded Image 4.png from disk
Image 4.png has image data of [[Loaded image data of Image 4.png]]
Loaded Image 5.png from disk
Image 5.png has image data of [[Loaded image data of Image 5.png]]

First gets loaded, then displays each at 1 sec interval.
"""