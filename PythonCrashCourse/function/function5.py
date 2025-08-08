def city_country(city, country):
    location_info = f"{city}, {country}"
    return location_info.title()

cidade1 = city_country("Itapetininga", "Brazil")
cidade2 = city_country("Londres", "Paris")
cidade3 = city_country("Paris", "France")

print(cidade1)
print(cidade2)
print(cidade3)
    