# Calculate the logarithm of a number
from math import log

def calculate_logarithm(number, base):
    """
    Calculates the logarithm of a number to a specified base.

    Args:
        number (float): The number to calculate the logarithm of.
        base (float): The base of the logarithm.

    Returns:
        float: The logarithm of the number to the specified base.
    """
    x=log(number,base)
    return x
print(calculate_logarithm(8,2))