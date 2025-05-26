from decimal import DivisionByZero


def add(number_1: float, number_2: float) -> float:
    """find the sum of two numbers"""
    return number_1 + number_2


def subtract(number_1: float, number_2: float) -> float:
    """subtract two numbers"""
    return number_1 - number_2


def multiply(number_1: float, number_2: float) -> float:
    """multiply two numbers"""
    return number_1 * number_2


def divide(number_1: float, number_2: float) -> float:
    """divide two numbers"""
    try:
        return number_1 / number_2

    except DivisionByZero:
        print("error. cant divide by 0")
