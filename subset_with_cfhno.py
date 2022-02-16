from ase import io
import inspect
import ase
from compare_homos import get_full_path
import functools

get_full_path = functools.partial(get_full_path, base_dir="data/OE62_5k")

molecules = io.read("df_5k_with_energies.xyz", index=":")

class XYZ_writer:
    def __init__(self, xyz_per_file=100):
        self.file_counter = 0
        self._xyz_counter = 0
        self.xyz_per_file = xyz_per_file

    def xyz_counter(self, value):
        if self._xyz_counter == self.xyz_per_file:
            self._xyz_counter = 0
            self.file_counter += 1
        else:
            self._xyz_counter = value
           
    def write(self, mol, i):
        self.xyz_counter(self._xyz_counter+1)
        with open(get_full_path("subsets/df_5k_subset_%d_with_energies.xyz" % self.file_counter), "a") as f, open(get_full_path("subsets/df_5k_subset_%d_indices.txt") % self.file_counter, "a") as f2:
            # uses ase versin 3.13 probably because I am writing this in python  2.7
            # I need to specify the columns to prevent it from printing everything
            # argument plain=True doesn't exit. (it exists in ase version 3.19)
            io.xyz.write_xyz(f, mol, comment="index=%d" % i, columns=['symbols', 'positions'], append=True)
            f2.write(str(i)+"\n")

xyz_writer = XYZ_writer(xyz_per_file = 1000)

for i, mol in enumerate(molecules):
    if set(mol.get_chemical_symbols()).issubset(["C","F","H","N","O"]):
        xyz_writer.write(mol, i) 


