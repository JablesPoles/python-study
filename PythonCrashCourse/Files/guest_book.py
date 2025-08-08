filename = '/home/fatec/Documentos/Estudo/Files/guest_book.txt'

with open(filename, "a") as file_object:
    while True:
        print("Enter 'quit' to exit.\n")
        user = input("Please enter your name: \n")
        if(user != "quit"):
            print(f"{user} welcome back!\n")
            file_object.write(f"{user}\n")
        else:
            break