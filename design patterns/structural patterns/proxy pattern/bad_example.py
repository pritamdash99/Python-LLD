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

class PhotoGallery:
    def __init__(self) -> None:
        self.__images : list[HighResolutionImage] = []

    def add_image(self, filename: str):
        highResImage = HighResolutionImage(filename)
        self.__images.append(highResImage)

    def displayGallery(self):
        for image in self.__images:
            image.display_image()

gallery = PhotoGallery()
gallery.add_image("Image 1.png")
gallery.add_image("Image 2.png")
gallery.add_image("Image 3.png")
gallery.add_image("Image 4.png")
gallery.add_image("Image 5.png")
"""
Loaded Image 1.png from disk
Loaded Image 2.png from disk
Loaded Image 3.png from disk
Loaded Image 4.png from disk
Loaded Image 5.png from disk

Every load happened at 1 sec interval.
ISSUE - 
We haven't displayed the gallery yet, but the photos seem to be loaded and ready for display.
The loading is happening just after each HighResolutionImage object creation.
"""

#gallery.displayGallery()


