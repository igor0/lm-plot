import itertools
import os
import pandas as pd
import re

class MetaExtractor:
    def from_run_id(self, run_id):
        return {}

    def from_config(self, config):
        return {}


class ConfigExtractor(MetaExtractor):
    def from_run_id(self, run_id):
        return {}

    def from_config(self, config):
        model = os.path.basename(config['model_args']['load'])
        return {
            'model': model
        }

    def columns(self):
        return [('model', str)]

class Model(MetaExtractor):
    def from_run_id(self, run_id):
        return {
            'model': run_id,
        }

    def columns(self):
        return [('model', str)]

class ModelStep(MetaExtractor):
    def __init__(self):
        self.rgx = re.compile("^(.*)-global_step(\d+)$")

    def from_run_id(self, run_id):
        m = self.rgx.match(run_id)
        if m is None:
            return None

        return {
            'model': m[1],
            'step': int(m[2]),
        }

    def columns(self):
        return [
            ('model', str),
            ('step', pd.Int64Dtype())
        ]

class Combiner(MetaExtractor):
    def __init__(parser_list):
        self.parser_list = parser_list

    def from_run_id(self, run_id):
        for meta_extractor in self.parser_list:
            out = meta_extractor.from_run_id(run_id)
            if out is not None:
                return out
        return None

    def columns(self):
        cols = []

        for meta_extractor in self.parser_list:
            cols.append(meta_extractor.columns())

        return list(itertools.chain.from_iterable(cols))
