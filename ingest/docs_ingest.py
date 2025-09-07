# ingest/fetch_cells.py
from allensdk.core.cell_types_cache import CellTypesCache
from pathlib import Path

out = Path("data"); out.mkdir(exist_ok=True, parents=True)
ctc = CellTypesCache(manifest_file=out/"manifest.json")

# Example: mouse, visual cortex (VISp), 20 cells
cells = ctc.get_cells(species=['Mus musculus'], structure__name='VISp')
cells = cells[:20]

for c in cells:
    sid = c['id']                  # specimen_id
    nwb_path = ctc.get_ephys_data(sid, file_name=out/f"{sid}.nwb")
    swc_path = ctc.get_reconstruction(sid, file_name=out/f"{sid}.swc")