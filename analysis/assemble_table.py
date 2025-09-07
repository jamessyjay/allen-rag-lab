import pandas as pd, glob, os
from .morpho_features import morpho_features
from .ephys_features import ephys_features


def assemble_table():
    rows=[]
    for nwb in glob.glob("data/*.nwb"):
        sid = os.path.basename(nwb).split(".")[0]
        ef = ephys_features(nwb).mean(numeric_only=True)  # average by sweeps
        mf = morpho_features(f"data/{sid}.swc")
        meta = {...}  # pull from manifest/cells or NWB attrs (layer, cre_line,…)
        row = {"specimen_id": sid, **ef.to_dict(), **mf.iloc[0].to_dict(), **meta}
        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_parquet("data/cell_features.parquet")
    return df