import json
import pandas as pd

from lm_plot.eval import _Eval
from lm_plot.files.collector import _collect

def collect(path_name, name_parser):
    data_dict = _collect(path_name, name_parser)
    
    df = pd.json_normalize(data_dict)
    for name, dtype in name_parser.columns():
        df[name] = df[name].astype(dtype)
    
    return _Eval(df)

def read_pickle(file_path):
    df = pd.read_feather(file_path)
    
    return _Eval(df)
