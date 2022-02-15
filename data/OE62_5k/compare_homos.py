import pdb
import json
import numpy as np
import click

prediction_files = ["/l/ghoshk1/rerunDTNN/%s/OE62_5k_output_subset_0/test_predictions.npz", "/l/ghoshk1/rerunDTNN/%s/OE62_5k_output_subset_1/test_predictions.npz","/l/ghoshk1/rerunDTNN/%s/OE62_5k_output_subset_2/test_predictions.npz"]

index_files = ["/l/ghoshk1/rerunDTNN/data/OE62_5k/subsets/df_5k_subset_0_indices.txt", "/l/ghoshk1/rerunDTNN/data/OE62_5k/subsets/df_5k_subset_1_indices.txt", "/l/ghoshk1/rerunDTNN/data/OE62_5k/subsets/df_5k_subset_2_indices.txt"]
xyz_files = ["/l/ghoshk1/rerunDTNN/data/OE62_5k/subsets/df_5k_subset_0_with_energies.xyz", "/l/ghoshk1/rerunDTNN/data/OE62_5k/subsets/df_5k_subset_1_with_energies.xyz", "/l/ghoshk1/rerunDTNN/data/OE62_5k/subsets/df_5k_subset_2_with_energies.xyz"]
homo_file = "/l/ghoshk1/rerunDTNN/data/OE62_5k/df_5k_homo.txt"

def load_indices(index_file):
    return np.genfromtxt(index_file, dtype=np.int32)

def load_prediction(file_path):
    return np.load(file_path)['y_pred']

def load_predictions(prediction_files, prediction_dir):
    preds = []
    for f in prediction_files:
        preds.append(load_prediction(f % prediction_dir))
    return np.vstack(np.array(preds))

def get_homo_to_homo_n(homos, n):
    """
    Since each set of HOMOs for a molecule could have different number of HOMO levels
    we pre-process it so that all molecules have same number of HOMOs
    Returns HOMO, HOMO-1,..., HOMO-n for each molecule"""
    ret_vals = []
    for idx, h in enumerate(homos):
        assert n <= len(h), "Atleast one molecule doesn't have n energy. \nindex = %d \nlevels = %d \n%s" % (idx, len(h), str(h))
        # pick the last n
        ret_val = h[-n:]
        # reverse: since we just want the highest energy homo values which are at the end.
        #ret_vals.append(ret_val[::-1])
        ret_vals.append(ret_val)
    # values are saved as HOMO-j, ...., HOMO-n, ..., HOMO, i.e. reversed
    return np.asarray(ret_vals)

class HOMO:
    def __init__(self, path_to_homo_file):
        self.path = path_to_homo_file
        self.homos = self.load_homos(self.path)

    def load_homos(self, path):
        homos = []
        with open(path, "r") as f:
            for l in f.readlines():
                homos.append(json.loads(l))
        return np.array(homos)

    def get_homo(self, index):
        return self.homos[index]

    def get_homos(self):
        return self.homos

@click.command()
@click.option('--energies', 'output_dir', help="Compare the predicted energies with target", flag_value="OE62_5k_energies_output", required=True)
@click.option('--spectra', 'output_dir', help="Compare the predicted spectra with target", flag_value="OE62_5k_spectra_output", required=True)
@click.option('--output_dir_suffix', help="Suffix added to the output directory name to compare data in different directories.", default="")

@click.option('-n', default=8, help="Number of homo values per molecule to compare")
def main(output_dir, n, output_dir_suffix):
    output_dir = output_dir + output_dir_suffix
    print output_dir
    homo_values = HOMO(homo_file)
    sum_sq_error = 0
    for idx_file, prediction_file in zip(index_files, prediction_files):
        indices = load_indices(idx_file)
        homos = homo_values.get_homo(indices)
        target = get_homo_to_homo_n(homos, n)
        predicted = load_prediction(prediction_file % (output_dir))
        predicted = predicted[:,-n:]
        # I should have used DTNN energy prediction.
        # energy code is in /l/ghoshk1/thesis/experiments/Annika_new_132k/deep_tensor_energies_mse_cost_optimized_multiple_RUNS
        print(target[0], predicted[0])
        sum_sq_error += np.mean((target-predicted) ** 2)
    
    print(sum_sq_error)
    print "RMSE for energies %0.5f" % np.sqrt(sum_sq_error/3)

if __name__ == "__main__":
    main()

