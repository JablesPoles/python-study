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

user1.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user2.increment_login_attempts()
user1.reset_login_attempts()
print(user1.login)
print(user2.login)


        