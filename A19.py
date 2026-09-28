# ---- Music Playlist Manager ----

class Playlist:

    # step 1 - Parameterized constructor: runs the moment the playlist object is created
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}'({self.genre}) is ready!")
    # STEP 2 - Add a song to the playlist

    def add_song(self, song):
        self.songs.append(song)
        print(f"'{song}' added to {self.name}.")

    # STEP 3 - Remove a song from the playlist
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed.")
        else:
            print(f"'{song}' not found in playlist.")

    # STEP 4 - Display all songs
    def display_songs(self):
        print(f"\n--- {self.name} ({self.genre}) ---")
        if self.songs:
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")
        else:
            print("No songs in the playlist. Add some songs to get started!")

    # STEP 5 - Destructor: runs automatically when the playlist is deleted
    def __del__(self):
        print(f"Playlist '{self.name}' is deleted. Goodbye!")

# Object Creation (constructor fires here)
my_playlist = Playlist("Chill Vibes", "Lo-fi")

# STEP 6 - Menu-driven program using the playlist class
while True:
    print("\n1. Add a song 2. Remove Song 3. View Playlist 4. Delete & Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        song = input("Enter the song name to add: ")
        my_playlist.add_song(song)
    elif choice == '2':
        song = input("Enter the song name to remove: ")
        my_playlist.remove_song(song)
    elif choice == '3':
        my_playlist.display_songs()
    elif choice == '4':
        del my_playlist # Destructor fires here
        break
    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")