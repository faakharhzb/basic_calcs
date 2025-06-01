"""basic_calcs is a python library for basic calculations. It has no dependencies, just the standard library. It can run on almost any OS or python version."""

import math


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

    result = numbers[0] - add(numbers[1:])
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


def area_triangle(length: float, breadth: float, verbose: bool = False) -> float:
    """find the area of a triangle"""

    result = length * breadth * (1 / 2)
    return (
        result
        if not verbose
        else f"area of an triangle with length {length} and breadth {breadth} = {result}"
    )


def area_quad(length: float, breadth: float, verbose: bool = False) -> float:
    """find the area of a quadrilateral"""

    result = length * breadth
    return (
        result
        if not verbose
        else f"area of an quadrilateral with length {length} and breadth {breadth} = {result}"
    )


def area_circle(radius: float, verbose: bool = False) -> float:
    """Find the area of a circle based on the given radius."""

    result = math.pi * (radius**2)
    return (
        result
        if not verbose
        else f"The area of a circle with radius {radius} = {result}"
    )


def area_polygon(side_length: float, num_sides: int, verbose: bool = False) -> float:
    """finds the area of a regular polygon"""

    if num_sides <= 2:
        raise ValueError("error. number of sides must be at least 3")

    result = ((side_length**2) * num_sides) / (
        4 * math.tan(math.radians(180 / num_sides))
    )
    return (
        result
        if not verbose
        else f"the area of a polygon with {num_sides} sides, each {side_length} long = {result}"
    )
