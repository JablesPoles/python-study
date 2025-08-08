filename = '/home/fatec/Documentos/Estudo/Files/guest.txt'

with open(filename, "a") as file_object:
    user_name = input("Write your username: \n")
    file_object.write(user_name)

