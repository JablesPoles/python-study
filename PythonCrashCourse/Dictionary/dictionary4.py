dictionary = {
    "if": "Conditional operator",
    "and": "Boolean operator",
    "or": "Boolean operator",
    "python": "Programing language",
    "for": "Repetition operator",
    }

for code, definitions in dictionary.items():
    print(f"{code.title()} is an {definitions.lower()}")
