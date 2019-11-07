"""
pdb.py
A python package for loading and writing data files
For the MolSSI Best Practices Workshop.

Handles the primary functions
"""
#
# import libraries
import numpy as np
import matplotlib.pyplot as plt


def open_pdb(file_location):
    """
    This function opens and reads in a pdb file and returns the atom names and coordinates.

    The pdb file must specify the atom elements on the last column,
    while has the atom coordinates in columns 30 to 55


    Parameters
    ----------
    file_location : str
        file path of the pdb data file

    Returns
    -------
    symbols: list of str
        List of string containing the symbol of each atom in the molecule
    coords: np.ndarray
        Matrix with the 3d coordinates of each atom in the molecule

    Examples
    --------
    """

    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []

    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(l[76:79].strip())
            atom_coords = [float(x) for x in l[30:55].split()]
            coordinates.append(atom_coords)

    coords = np.array(coordinates)
    return symbols, coords


