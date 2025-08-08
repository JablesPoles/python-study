import json

filename = 'favorite_num.json'

favorite_number = int(input("Write your favorite number: "))
with open (filename, 'w') as f:
    json.dump(favorite_number, f)
    