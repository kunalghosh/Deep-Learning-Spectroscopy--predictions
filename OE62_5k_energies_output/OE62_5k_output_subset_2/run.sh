model_path=$PWD/../../pretrained_model/energies/2017-07-14_10-39-54
data_path=$PWD/../../data/OE62_5k/subsets/df_5k_subset_2_with_energies.xyz
OMP_NUM_THREADS=8 THEANO_FLAGS=mode=FAST_RUN,device=cpu,floatX=float32,openmp=True python $PWD/../../Deep-Learning-Spectroscopy/deep_tensor_refactored/predict.py --clen 36 --batch_size 50 --num_neu_1 300 --num_neu_2 550 --model_name model_neu1_neu2_with_noise $data_path $model_path/results/model_epoch1528.pkl.gz $model_path/Y_vals.npz
