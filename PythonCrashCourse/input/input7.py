sandwich_orders = ["Calabresa", "Bacon", "Bauru"]
finished_sandwiches = []

while sandwich_orders:
    ready = sandwich_orders.pop()
    print(f"Your {ready} is done.")
    finished_sandwiches.append(ready)
        
for done_sandwich in finished_sandwiches:
    print(f"These are the finished sandwiches {done_sandwich}")
        
        
