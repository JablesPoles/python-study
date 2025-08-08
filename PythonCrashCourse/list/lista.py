placas_video = ["GTX 1080", "RTX 2080", "RX 6600XT"]
print(f"My first graphics card was and {placas_video[0]} eventually i bought an {placas_video[2]}")

dinner_guests = ["Joey", "Escriba", "Guizão"]
print (f"This is an invite for these weird fuckos:\n {dinner_guests[1]}, you are invited to the peleja\n {dinner_guests[0]}, you are invited for a hug\n {dinner_guests[2]} you are invited to kiss my ass\n")
print (f"Oh shit, {dinner_guests[2]} won't show up to kiss my ass\n")

dinner_guests[2] = "Leozin"
print (f"This is an invite for these weird fuckos:\n {dinner_guests[1]}, you are invited to the peleja\n {dinner_guests[0]}, you are invited for a hug\n {dinner_guests[2]} you are invited to not use drugs in my bathroom\n")
print ("Found some new spots for the peleja boys")

dinner_guests.insert(0, "Luiz")
dinner_guests.insert(2, "Kae")
dinner_guests.append("Nero")
print (f"This is an invite for these weird fuckos:\n {dinner_guests[3]}, you are invited to the peleja\n {dinner_guests[1]}, you are invited for a hug\n {dinner_guests[4]} you are invited to not use drugs in my bathroom\n {dinner_guests[0]}, you are invited to meet us\n {dinner_guests[2]}, if you talk about manhwas i'm gonna kick your throat\n {dinner_guests[5]}, you are not invited")
excluidos = dinner_guests.pop(0)
print(f"I'm sorry {excluidos}, i don't have space anymore.")
excluidos = dinner_guests.pop(1)
print(f"I'm sorry {excluidos}, i don't have space anymore.")
excluidos = dinner_guests.pop(2)
print(f"I'm sorry {excluidos}, i don't have space anymore.")
excluidos = dinner_guests.pop(2)
print(f"I'm sorry {excluidos}, i don't have space anymore.")

print(f"So, just the two of you, yes {dinner_guests[0]}, you are still invited, i was considering not inviting {dinner_guests[1]}, but you are still in too.")

del dinner_guests[0]
del dinner_guests[0]

print(dinner_guests)
