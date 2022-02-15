cd pretrained_model/spectra/
curl -o spectra.tar.gz https://zenodo.org/record/6091030/files/deep_tensor_spectra_mse_cost_optimized_re-run_2018-11-27_15-22-42.tar.gz 
tar -xvzf spectra.tar.gz 
cd ../..

cd pretrained_model/energies/
curl -o energies.tar.gz https://zenodo.org/record/6091030/files/deep_tensor_energies_mse_cost_optimized_multiple_RUNS_2017-07-14_10-39-54.tar.gz
tar -xvzf energies.tar.gz
cd ../..

git clone https://github.com/kunalghosh/Deep-Learning-Spectroscopy

cd data/132k_16_opt_eV
wget https://zenodo.org/record/3386508/files/132k_16_opt_eV.tar.gz
tar -xvzf 132k_16_opt_eV.tar.gz
cd ../..
