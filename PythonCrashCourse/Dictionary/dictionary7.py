escriba = {"first_name": "fernando", "last_name": "thibes"}
guizao = {"first_name": "guilherme", "last_name": "leme"}
joey = {"first_name": "jonatas", "last_name": "machado"}
user_data = [escriba, guizao, joey]

for name in (user_data):
    print(f"\nName: {name['first_name']} {name.get('last_name', '404')}")



