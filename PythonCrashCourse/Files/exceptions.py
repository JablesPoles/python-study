print("Input two numbers or 'q' to exit: \n")

while True:
    try:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        numbers = num1 + num2
    except ValueError:
        print("One of the inputs was not a number.")
    else: 
        print(f"The sum of the numbers is: {numbers}")