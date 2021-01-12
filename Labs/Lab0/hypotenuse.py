import math


def calculateHypotenuse(side1: int, side2: int):
    hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
    return hypotenuse


def sum(num1: int, num2: int):
    return num1 + num2


def multiply(num1: int, num2: int):
    return num1 * num2


def divide(num1: int, num2: int):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Can't divide by zero!")


def subtract(num1: int, num2: int):
    return num1 - num2


def main():
    print("Hello")


if __name__ == '__main__':
    main()
    option = int(input("""1 to calculate hypotenuse 
2 to add 
3 to subtract 
4 to multiply 
5 to divide\n"""))

    if option == 1:

        value1 = int(input("Enter first number: "))
        value2 = int(input("Enter second number: "))
        result = calculateHypotenuse(value1, value2)
        print(result)

    elif option == 2:

        value1 = int(input("Enter first number"))
        value2 = int(input("Enter second number"))
        result = sum(value1, value2)
        print(result)

    elif option == 3:

        value1 = int(input("Enter first number"))
        value2 = int(input("Enter second number"))
        result = subtract(value1, value2)
        print(result)

    elif option == 4:

        value1 = int(input("Enter first number"))
        value2 = int(input("Enter second number"))
        result = multiply(value1, value2)
        print(result)

    else:

        value1 = int(input("Enter first number"))
        value2 = int(input("Enter second number"))
        result = divide(value1, value2)
        print(result)
