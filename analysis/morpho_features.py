import neurom as nm
import pandas as pd


def morpho_features(swc_file):
    nrn = nm.load_morphology(swc_file)
    soma = nm.get('soma_radius', nrn)
    n_branch = nm.get('number_of_bifurcations', nrn)
    path_len = nm.get('total_length', nrn)
    return pd.DataFrame([{
        "soma_radius": float(soma),
        "bifurcations": int(n_branch),
        "total_length": float(path_len),
    }])