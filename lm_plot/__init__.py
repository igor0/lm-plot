import json
import pandas as pd

from lm_plot.eval import _LMEval
from lm_plot.files.collector import _collect

def collect(path_name, meta_extractor):
    data_dict = _collect(path_name, meta_extractor)
    
    df = pd.json_normalize(data_dict)
    for name, dtype in meta_extractor.columns():
        if name in df:
            df[name] = df[name].astype(dtype)
    
    return _LMEval(df)

def read_feather(file_path):
    df = pd.read_feather(file_path)
    
    return _LMEval(df)
