import math
def calculator():
    print("Simple Calculator")
    print("1. Addition Operation")
    print("2. Subtraction Operation")
    print("3. Multiplication Operation")
    print("4. Division Operation")
    print("5. Square Root Operation")
    print("6. Cube Root Operation")
    print("7. Sine Operation")
    print("8. Cosine Operation")
    print("9. Floor Operation")
    try:
        choice = int(input("Enter choice (1/2/3/4/5/6/7/8/9): "))
        if choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Invalid choice.")
            return
        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        else:
            num1 = float(input("Enter a number: "))
        if choice == 1:
            print(num1, "+", num2, "=", num1 + num2)
        elif choice == 2:
            print(num1, "-", num2, "=", num1 - num2)
        elif choice == 3:
            print(num1, "*", num2, "=", num1 * num2)
        elif choice == 4:
            if num2 != 0:
                print(num1, "/", num2, "=", num1 / num2)
            else:
                print("Cannot divide by zero")
        elif choice == 5:
            print("sqrt(", num1, ") =", math.sqrt(num1))
        elif choice == 6:
            print("cbrt(", num1, ") =", math.pow(num1, 1/3))
        elif choice == 7:
            print("sin(", num1, ") =", math.sin(math.radians(num1)))
        elif choice == 8:
            print("cos(", num1, ") =", math.cos(math.radians(num1)))
        elif choice == 9:
            print("floor(", num1, ") =", math.floor(num1))
    except ValueError:
        print("Invalid input.")
calculator()
