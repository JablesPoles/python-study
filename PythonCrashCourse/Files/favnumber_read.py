import json

filename = 'favorite_num.json'

with open(filename) as f:
    favorite_number = json.load(f)
    print(f"I know your favorite number, it is {favorite_number}")