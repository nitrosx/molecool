"""
measure.py
A python package for analyzing molecules. 
For the MolSSI Best Practices Workshop.

Handles the primary functions
"""
#
# import libraries
import numpy as np


def calculate_distance(point_A, point_B):
    """
    This function calculates the distance between two points given as numpy arrays.
   
    Parameters
    ----------
    point_A, point_B : np.ndarray
        Space coordinates of the 2 molecules.

    Returns
    ------- 
    distance : np.float
        Euclidean distance between the two points.

    Examples
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([3.0, 0, 0])
    >>> calculate_distance(r1, r2)
    3.0
    """
    # this doc string are in numpy style

    distance_vector = (point_A - point_B)
    distance = np.linalg.norm(distance_vector)
    return distance


def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta


