class User:
    def __init__(self, first_name, last_name, birthdate, country, login_attempts = 0):
        self.fname = first_name
        self.lname = last_name
        self.birthdate = birthdate
        self.country = country
        self.login = login_attempts
        
    def increment_login_attempts(self):
        self.login += 1
        
    def reset_login_attempts(self):
        self.login = 0
        
    def describe_user(self):
        print(f"\nName: {self.fname} {self.lname}\nDate of Birth: {self.birthdate}\nCountry: {self.country}")
        
    def greet_user(self):
        print(f"\nGreetings {self.fname} {self.lname}!!")

user1 = User("Fernando", "Thibes", "25/05/2001", "Brazil")
user2 = User("Joey", "Deus", "13/07/1994", "UK")
user3 = User("Gabriela", "Mastrandea", "06/06/2006", "Argentina")

class Admin(User):
    def __init__(self, privileges, first_name, last_name, birthdate, country, login_attempts=0):
        super().__init__(first_name, last_name, birthdate, country, login_attempts)
        self.privileges = privileges
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        privileges = ["can add post", "can delete post", "can ban user"]
        print(f"These are the admin privileges: {self.privileges}")

print


        