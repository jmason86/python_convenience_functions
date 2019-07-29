import numpy as np


def lat_lon_to_position_angle(latitude, longitude):
    """Function to translate heliocentric coordinates (latitude, longitude) into position angle
    Written by Alysha Reinard and James Paul Mason.

    Inputs:
        longitude [float]: The east/west coordinate
        latitude [float]: The north/south coordinate

    Optional Inputs:
       None

    Outputs:
        position_angle [float]: The converted position angle measured in degrees from solar north, counter clockwise

    Optional Outputs:
        None

    Example:
        position_angle = lat_lon_to_position_angle(35, -40)
    """
    x = longitude * 1.0
    y = latitude * 1.0
    if y != 0:
        pa = np.arctan(-np.sin(x) / np.tan(y))
    else:
        pa = 3.1415926 / 2.  # limit of arctan(infinity)

    pa = pa * 180.0 / 3.1415926

    if y < 0:
        pa += 180
    if x == 90 and y == 0:
        pa += 180
    if pa < 0:
        pa += 360

    if x == 0 and y == 0:
        pa = -1

    return pa
