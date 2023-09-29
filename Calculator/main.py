def A(x, y):
    return x + y

def B(x, y):
    return x - y

def C(x, y):
    return x * y

def D(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("\n============ Mini Calculator ==============\n")
    print("Options:\n")
    print(" * Enter '1' for addition")
    print(" * Enter '2' for subtraction")
    print(" * Enter '3' for multiplication")
    print(" * Enter '4' for division")
    print(" * Enter 'quit' to end the program")

    user_input = input(" \n Enter Your Choice From 1-4  : ")

    if user_input == "quit":
        break
    elif user_input in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "1":
            print("Addition:", A(num1, num2))
        elif user_input == "2":
            print("Subtraction:", B(num1, num2))
        elif user_input == "3":
            print("Multiplication:", C(num1, num2))
        elif user_input == "4":
            print("Division:", D(num1, num2))
    else:
        print("Invalid input")

