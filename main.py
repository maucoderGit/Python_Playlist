from playlist_proyect import Playlist
from Song import Song
from time import sleep


def add_song_by_console():
    song_by: str = str(input("Who created the song: "))
    name: str = str(input("Song's name: "))
    time_of_song: int = int(input("How long is the song (in seconds): "))
    
    validator = True

    while validator == True:
        ft_singer:str = input("Do you want to add ft? Y/N: ")

        if ft_singer.upper() == "Y":
            ft_singer = input("Name of the artist/artists: ")
            break

        elif ft_singer.upper() == "N":
            ft_singer = None
            break
        else:
            print("Please insert Y or N")
            validator = True
    
    print("Your song upload was complete!")

    return Song(song_by, name, time_of_song, ft_singer)

def run():
    my_playlist = Playlist("Maucoder PlayList")
    cancion = add_song_by_console()
    my_playlist.add_song(cancion)

    print(my_playlist.play_song(cancion.name))

if __name__ == "__main__":
    run()