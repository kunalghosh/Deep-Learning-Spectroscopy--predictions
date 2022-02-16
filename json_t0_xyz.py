import json
import pandas as pd
from compare_homos import get_full_path
import functools

get_full_path = functools.partial(get_full_path, base_dir="data/OE62_5k")

df_5k = pd.read_json(get_full_path("df_5k.json"), orient="split")

with open(get_full_path("df_5k_with_energies.xyz"), "w") as f, open(get_full_path("df_5k_homo.txt"), "w") as f2:
    for i, row in df_5k.iterrows():
        xyz = row.xyz_pbe_relaxed.split("\n")
        xyz[1] = str(row['energies_occ_pbe'])
        xyz="\n".join(xyz)
        f.write(xyz)
        f2.write(json.dumps(row['energies_occ_pbe'])+"\n")
