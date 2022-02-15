import json
import pandas as pd

df_5k = pd.read_json("df_5k.json", orient="split")

with open("df_5k_with_energies.xyz", "w") as f, open("df_5k_homo.txt", "w") as f2:
    for i, row in df_5k.iterrows():
        xyz = row.xyz_pbe_relaxed.split("\n")
        xyz[1] = str(row['energies_occ_pbe'])
        xyz="\n".join(xyz)
        f.write(xyz)
        f2.write(json.dumps(row['energies_occ_pbe'])+"\n")
