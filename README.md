# Deep-Learning-Spectroscopy--predictions
Repo to make predictions using the deep learning spectroscopy code

1. Clone the repo and execute `setup.sh` to download the necessary data and set up the directories
2. execute `OE62_5k_energies_output/OE62_5k_output_subset_0/run.sh` to make predictions on a subset of data (subsets computed using [script](https://github.com/kunalghosh/Deep-Learning-Spectroscopy--predictions/blob/main/data/OE62_5k/subset_with_cfhno.py) - it keeps only molecules with C,F,H,N,O because the original model was trained only on molecules with these species.
3. execute `OE62_5k_energies_output/OE62_5k_output_subset_1/run.sh` and
4. `OE62_5k_energies_output/OE62_5k_output_subset_2/run.sh`
5. Finally run [compare_homos.py](https://github.com/kunalghosh/Deep-Learning-Spectroscopy--predictions/blob/main/compare_homos.py) to compare predicted and target HOMO values. some molecules in OE62 have only 8 HOMO levels so the comparison script takes only the highest 8.
