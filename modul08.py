# Convert an angle from degrees to radians
from math import radians

def convert_degrees_to_radians(degrees):
    """
    Converts an angle from degrees to radians.

    Args:
        degrees (float): The angle in degrees.

    Returns:
        float: The angle in radians.
    """
    x=radians(degrees)
    return x
print(convert_degrees_to_radians(90))