class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        
    def describe_restaurant(self):
        print(f"The restaurant name is {self.name}, it is a {self.type} diner and it has served {served} people!")
    
    def open_restaurant(self):
        print(f"{self.name} is open")
        
restaurant1 = Restaurant("Barbosa", "Hot Dog")
restaurant2 = Restaurant("Kozan", "Sushi")
restaurant3 = Restaurant("São João", "Padaria")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()