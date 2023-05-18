# Round a decimal number to the nearest integer
from math import trunc

def round_to_nearest_integer(number):
    """
    Rounds a decimal number to the nearest integer.

    Args:
        number (float): The decimal number.

    Returns:
        int: The nearest integer.
    """
    x=round(number)
    return x
print(round_to_nearest_integer(3.7))