def add(number_1: float, number_2: float, verbose: bool=False) -> float:
    """find the sum of two numbers"""
    result = number_1 + number_2
        return result if not verbose else f"{number_1} + {number_2} = {result}"


def subtract(number_1: float, number_2: float, verbose: bool=False) -> float:
    """subtract two numbers"""
    result = number_1 - number_2
        return result if not verbose else f"{number_1} - {number_2} = {result}"


def multiply(number_1: float, number_2: float, verbose: bool=False) -> float:
    """multiply two numbers"""
    result = number_1 * number_2
        return result if not verbose else f"{number_1} × {number_2} = {result}"


def divide(number_1: float, number_2: float, verbose: bool=False) -> float:
    """divide two numbers"""
    try:
					result = number_1 / number_2
        return result if not verbose else f"{number_1} ÷ {number_2} = {result}"

    except ZeroDivisionError:
        print("error. cant divide by 0")
