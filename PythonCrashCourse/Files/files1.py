import os

dest = os.path.dirname(os.path.abspath(__file__))
os.chdir(dest)

def show_content(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        print(f"The file {filename} has these animal names: {words}")

filenames: ['cats.txt', 'dogs.txt']
for filename in filenames:
    show_content(filename)