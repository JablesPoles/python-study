animals = ["Thalycea", "Willy mammoth", "Dodo", "Leviathan whale", "Megalodon"]

for animals in animals:
    print(f"The {animals} is an extinct animal")
print("All of these are being ressurected by Colossal")

print(f"The first three animal in the list are:")
for animal in animals[:3]:
    print(animal.title())
print("The middle animals in the list are:\n")
for animal in animals[1:4]:
    print(animal.title())
print("The last animals in the list are: \n")
for animal in animals[2:5]:
    print(animal.title())