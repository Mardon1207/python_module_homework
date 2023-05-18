# Calculate the power of a number
import math

def calculate_power(base, exponent):
    """
    Calculates the power of a number.

    Args:
        base (float): The base number.
        exponent (float): The exponent.

    Returns:
        float: The result of raising the base to the exponent.
    """
    return pow(base,exponent)
print(calculate_power(2,3))