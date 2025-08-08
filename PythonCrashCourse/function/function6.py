def make_album(artist, album, songs=None):
    description = {"name": artist, "album": album}
    if songs:
        description = {"name": artist, "album": album, "songs": songs}
    return description

album1 = make_album("System of a Down", "Hypnotize", songs = 5)
album2 = make_album("Slipknot", "Iowa")
album3 = make_album("Linkin Park", "Hybrid Theory")

print(album1)
print(album2)
print(album3)


    
    
    