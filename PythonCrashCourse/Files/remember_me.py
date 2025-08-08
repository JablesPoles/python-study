import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for a new username."""    
    username = input("What is your username? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
        
    
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}!")
    else:
        username = get_new_username()
        print(f"We'll remeber you when you come back, {username}")

username = get_stored_username()
ask = input(f"Is {username} your username? (Yes/No) ")
if(ask == "Yes"):            
    greet_user()
elif(ask == "No"):
    get_new_username()
    username = get_stored_username()
    print(f"Welcome {username}!")
else:
    print("Answer (Yes/No) to continue!") 