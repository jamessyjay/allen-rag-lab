from ipfx.feature_extractor import FeatureExtractor
from ipfx.nwb_data_set import NwbDataSet


def ephys_features(nwb_file):
    ds = NwbDataSet(nwb_file)
    sweeps = ds.get_sweep_numbers()
    # TODO: chose depolarizing current injections
    fe = FeatureExtractor.from_nwb(nwb_file)
    feats = fe.extract()    # will give membrane/ spikes features
    return feats.to_dataframe()