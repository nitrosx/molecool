"""
test molecule module
"""

import pytest
import molecool
import numpy as np


def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])

    #assert center_of_mass.all() == expected_center.all()
    assert np.array_equal(center_of_mass, expected_center)



def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']
    
    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = sum([
        molecool.data.atomic_weights[atom]
        for atom 
        in symbols])
    
    assert actual_mass == calculated_mass
