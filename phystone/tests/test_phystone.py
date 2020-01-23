"""
Unit and regression test for the phystone package.
"""

# Import package, test suite, and other packages as needed
import phystone
import pytest
import sys

def test_phystone_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "phystone" in sys.modules

#Tests for transmutations.py
from ase import Atom, Atoms
from ase.build import fcc111, add_adsorbate
from ase.visualize import view

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
transmute, counter = phystone.transmutations.index_transmuted(slab, 'Cu', 'Cu',
                                                              8, 1)
new_atom = Atom('Zn')
transmuted_slab = phystone.transmutations.transmuter(slab, transmute,
                                                     [new_atom]*len(transmute))

symmetric_slab = fcc111('Cu', size=(2, 2, 9), vacuum=10.0, orthogonal=True)
symmetric_transmute, symmetric_counter = phystone.transmutations.index_transmuted(
    symmetric_slab,'Cu', 'Cu', 8, 1, symmetric=True)
print(symmetric_slab.get_center_of_mass())
print(symmetric_slab[17].position[2])
from numpy import isclose
print(isclose([symmetric_slab[17].position[2]],[symmetric_slab.get_center_of_mass()[2]]))
#view(symmetric_slab)
print(symmetric_transmute, symmetric_counter)