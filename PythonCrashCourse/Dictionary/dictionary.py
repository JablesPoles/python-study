escriba = {"first_name": "fernando", "last_name": "thibes", "city": "itapetininga"}
first_name = escriba.get("first_name")
last_name = escriba.get("last_name")
city = escriba.get("city")

print(f"Escriba's first name is {first_name.title()}")
print(f"Escriba's last name is {last_name.title()}")
print(f"Escriba's city is {city.title()}")
