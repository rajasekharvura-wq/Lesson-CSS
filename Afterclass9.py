class ArtGallery:
    def __init__(self, name):
        self.name = name
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print("Artwork added!")

    def show_artworks(self):
        if self.artworks:
            for artwork in self.artworks:
                print("-", artwork)
        else:
            print("No artworks yet.")

    def __del__(self):
        print("Gallery closed.")


gallery = ArtGallery("My Art Gallery")

while True:
    print("\n1. Add Artwork")
    print("2. Show Artworks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        artwork = input("Enter artwork name: ")
        gallery.add_artwork(artwork)

    elif choice == "2":
        gallery.show_artworks()

    elif choice == "3":
        break

    else:
        print("Invalid choice.")
