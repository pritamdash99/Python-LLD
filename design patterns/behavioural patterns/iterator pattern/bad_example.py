# Bad Example

class Song:
    def __init__(self, title:str) -> None:
        self.__title = title

    def get_title(self):
        return self.__title

class Playlist:
    def __init__(self) -> None:
        self.__playlist : list[Song] = []

    def get_playlist(self) -> list[Song]:
        return self.__playlist

    def add_song(self, song : Song):
        self.__playlist.append(song)

playlist = Playlist()
playlist.add_song(Song("Song 1"))
playlist.add_song(Song("Song 2"))
playlist.add_song(Song("Song 3"))
playlist.add_song(Song("Song 4"))

#Now if you want to fecth the titles of all the songs - 
print("Titles are = ")
for i in range(len(playlist.get_playlist())):
    print (f"({i}) {playlist.get_playlist()[i].get_title()}")
"""
Titles are = 
(0) Song 1
(1) Song 2
(2) Song 3
(3) Song 4
"""

"""
Issue - 
Inside the Playlist constructor, if we change the 
    self.__playlist : list[Song] = [] 
    to 
    self.__playlist : set[Song] = set()

    and inside add_song() We add the songs as set.add() instead of list.append()

    We won't be able iterate over the set as it's unordered, we'll have to try another aproach. 
    
    So without the iterator pattern we had to make changes inside and outside the core code.
"""