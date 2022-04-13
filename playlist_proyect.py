from time import sleep
from nodes_based_queue import Queue

class Playlist():
    def __init__(self, name):
        self.name = name
        self.queue = Queue()
        self.size = self.queue.length()

    def add_song(self, Song):
        self.queue.enqueue(Song)

    def show_playlist(self):
        for i in self.queue.iter():
            print(i)

    def play_songs(self):
        if self.size == 0:
            return f'Playlist is empty, do you want to add any song?'
        else:
            probe = self.queue.head

            while probe != None:
                print(probe.data.show())
                sleep(probe.data.time)
                
                probe = probe.next
                print(f"Now playing next song: {probe.data.name}")

            return f"Nice songs! but i'm empty now D: \b Do you want to add more songs?"
        
    
    def play_song(self, name_song: str):
        probe = self.queue.head

        while probe != None:
            if probe.data.name.upper() != name_song.upper():
                probe = probe.next
            else:
                print(probe.data.show())
                sleep(probe.data.time)
                return "The song's end..."

        return f'I can not find {name_song} in your Playlist :('
            