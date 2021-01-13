import math


def calculateHypotenuse(side1: int, side2: int):
    """
    calculates the hypotenuse with two sides given.
    :param side1: int
    :param side2: int
    :return: hypotenuse
    """
    hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
    return hypotenuse


def add(num1: int, num2: int):
    """
    calculates the sum of two numbers.
    :param num1: int
    :param num2: int
    :return: num1 + num2
    """
    return num1 + num2


def multiply(num1: int, num2: int):
    """
    calculates the multiplication of two numbers.
    :param num1: int
    :param num2: int
    :return: num1 * num2
    """
    return num1 * num2


def divide(num1: int, num2: int) -> float:
    """
    calculates the division of two numbers.
    :param num1: int
    :param num2: int
    :return: num1 / num2
    """
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Can't divide by zero!")


def subtract(num1: int, num2: int):
    """
    calculates the subtraction of two numbers.
    :param num1: int
    :param num2: int
    :return: num1 - num2
    """
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
        result = add(value1, value2)
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
