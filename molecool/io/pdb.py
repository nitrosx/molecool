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
    # This function reads in a pdb file and returns the atom names and coordinates.
    with open(file_location) as f:
        data = f.readlines()
    coordinates = []
    sym = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            sym.append(l[76:79].strip())
            atom_coords = [float(x) for x in l[30:55].split()]
            coordinates.append(atom_coords)
    coords = np.array(coordinates)
    return sym, coords


