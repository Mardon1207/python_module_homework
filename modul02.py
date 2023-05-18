# Calculate the factorial of a number
import math

def calculate_factorial(number):
    """
    Calculates the factorial of a given number.

    Args:
        number (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the given number.
    """
    s=1
    while number>0:
        s=s*number
        number-=1
    return s
print(calculate_factorial(12))
