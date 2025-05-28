def add(numbers: list[float], verbose: bool = False) -> float:
    """find the sum of all the numbers in the list. for example:
    if the funtion is like basic_calcs.add([1, 4, 6, 8, 90]), it will find the sum of all the numbers, resulting in 109 as the answer"""

    result = sum(numbers)
    return (
        result if not verbose else f"{' + '.join(str(i) for i in numbers)} = {result}"
    )


def subtract(numbers: list[float], verbose: bool = False) -> float:
    """subtract all the numbers in the list. for example:
    if the funtion is like basic_calcs.subtract([100, 25, 10, 1]), it will subtract all the numbers from the first number, resulting in 64 as the answer"""

    result = numbers[0] - sum(numbers[1:])
    return (
        result if not verbose else f"{' - '.join(str(i) for i in numbers)} = {result}"
    )


def multiply(numbers: list[float], verbose: bool = False) -> float:
    """multiplies all the numbers in the list. for example:
    if the funtion is like basic_calcs.multiply([10, 5, 3, 2]), it will multiply all the numbers, resulting in 300 as the answer"""

    result = 1
    for i in numbers:
        result *= i

    return (
        result if not verbose else f"{' × '.join(str(i) for i in numbers)} = {result}"
    )


def divide(number_1: float, number_2: float, verbose: bool = False) -> float:
    """divide two numbers"""

    try:
        result = number_1 / number_2
        return (
            result if not verbose else f"{'⌊', number_1} ÷ {number_2, '⌋'} = {result}"
        )

    except ZeroDivisionError:
        print("error. cant divide by 0")


def floor(number_1: float, number_2: float, verbose: bool = False) -> float:
    """performs floor division on two numbers"""

    try:
        result = int(number_1 // number_2)
        return result if not verbose else f"{number_1} ÷ {number_2} = {result}"

    except ZeroDivisionError:
        print("error. cant divide by 0")


def power(number_1: float, number_2: float, verbose: bool = False) -> float:
    """raise number_1 to the power of number_2"""

    result = number_1**number_2
    return (
        result if not verbose else f"{number_1} to the power of {number_2} = {result}"
    )


def root(number_1: float, number_2: float, verbose: bool = False) -> float:
    """finds the nth root of a number"""
    result = number_1 ** (1 / number_2)
    return result if not verbose else f"{number_1} √ {number_2} = {result}"
