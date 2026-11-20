from abc import ABC, abstractmethod

class Song:
    def __init__(self, title:str) -> None:
        self.__title = title

    def get_title(self) -> str:
        return self.__title

#Abstract Class
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool : pass #Checks if there is a next element to iterate over.

    @abstractmethod
    def next(self) -> Song | None: pass # To return the next element or None

# We need a iterator to iterate over a playlist
class Playlist_Iterator(Iterator):

    def __init__(self, song_list : list[Song]) -> None:
        self.__songList = song_list
        self.__position = 0

    def has_next(self) -> bool:
        if self.__position < len(self.__songList):
            return True
        return False
    
    def next(self) -> Song | None:  # "|" is Pipe operator, Either return Song Type OR None
        while self.has_next() == True:
            song = self.__songList[self.__position]
            self.__position += 1
            return song
        return None

# Now we create the playlist to iterate over using the playlist_iterator

class Playlist:
    def __init__(self) -> None:
        self.__playlist : list[Song] = []

    def add_song(self, song : Song):
        self.__playlist.append(song)

    def create_iterator(self) -> Playlist_Iterator:
        return Playlist_Iterator(self.__playlist)
    
# Now we create the objects and iterate over them
playlist = Playlist()
playlist.add_song(Song("Song 1"))
playlist.add_song(Song("Song 2"))
playlist.add_song(Song("Song 3"))
playlist.add_song(Song("Song 4"))

iterator = playlist.create_iterator() #This created the PlaylistIterator
'''
while iterator.has_next():
    print(iterator.next().get_title()) 
This is not working as "None" return type throws issue for .next() as there is a song to be returned on the 1st iteration
"None" requires handling.
'''
while iterator.has_next():
    song = iterator.next()
    if song is not None:
        print(song.get_title())

# Song 1
# Song 2
# Song 3
# Song 4