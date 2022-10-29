import json

class _Eval:
    def __init__(self, df):
        self.df_ = df
    
    def to_pickle(self, path):
        self.df_.to_feather(path)

    def pandas(self):
        return self.df_
