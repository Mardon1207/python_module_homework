# Convert an angle from radians to degrees
from math import degrees

def convert_radians_to_degrees(radians):
    """
    Converts an angle from radians to degrees.

    Args:
        radians (float): The angle in radians.

    Returns:
        float: The angle in degrees.
    """
    x=degrees(radians)
    return x
print(convert_radians_to_degrees(1.5707963267948966))