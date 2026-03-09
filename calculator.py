try:
    number1 = float(input("Insert first number:"))
    number2 = float(input("Insert second number:"))
    operations = input("Insert operation(+,-,*,/):")
    if operations == "+":
        print(number1 + number2)
    elif operations == "-":
        print(number1 - number2)
    elif operations == "*":
        print(number1 * number2)
    elif operations == "/":
        if number2 != 0:
            print(number1 / number2)
        else:
            print("number cannot be divided by zero")
    else:
        print("invalid operation")
except ValueError:
    print("Invalid Result")


