#We implement the iterator now as a linkedlist as backbone
from abc import ABC, abstractmethod

class Song:
    def __init__(self, title:str) -> None:
        self.__title = title

    def get_title(self) -> str:
        return self.__title

#Interface 
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool : pass #Checks if there is a next element to iterate over.

    @abstractmethod
    def next(self) -> Song | None: pass # To return the next element or None

#Node Class for linkedlist - contains Song Pointer to next Node
class Node:
    def __init__(self, song : Song) -> None:
        self.song : Song = song
        self.next : Node | None = None

# Playlist Iterator

class Playlist_Iterator(Iterator) :

    def __init__(self, head : Node | None) -> None:
        self.__current : Node | None = head

    def has_next(self) -> bool:
        #Checks if there is a next node
        return self.__current is not None

    def next(self) -> Song | None : 
        #Get current song and move to next node
        current = self.__current
        if current is None:
            return None
        song = current.song
        self.__current = current.next
        return song

#Playlist Creation
class Playlist:
    def __init__(self) -> None:
        self.__head : Node | None = None #First node
        self.__tail : Node | None = None #Last code

    def add_song(self, song : Song):
        #Add song to end of LL
        new_node = Node(song)
        if self.__head is None:
            #First Song - both head and tail point to it.
            self.__head = new_node
            self.__tail = new_node
        else:
            #Add to end - link current tail to new node
            assert self.__tail is not None      #assert keyword used for debugging
            self.__tail.next = new_node
            self.__tail = new_node

    def create_iterator(self) -> Playlist_Iterator:
        #Create iterator starting from head of Linked List
        return Playlist_Iterator(self.__head)

# You'll notice the main obeject creation part remains the same.

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

"""
Song 1
Song 2
Song 3
Song 4
"""

