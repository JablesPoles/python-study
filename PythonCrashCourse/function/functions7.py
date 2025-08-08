def make_album(artist, album, songs=None):
    description = {"name": artist, "album": album}
    if songs:
        description = {"name": artist, "album": album, "songs": songs}
    return description

while True:
    print("\nPress q to exit at any time")
    print("\nEnter an artist name and a album:")
    artist = input("Artist: ")
    if artist == "q":
        break
    album = input("Album: ")
    if album == "q":
        break
    
    fdescription = make_album(artist, album)
    print(fdescription)

    
    
    