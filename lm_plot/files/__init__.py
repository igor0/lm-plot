import itertools
import pandas as pd
import re

class NameParser:
    def parse(self, run_id):
        return None

class Model(NameParser):
    def parse(self, run_id):
        return {
            'model': run_id,
        }

    def columns(self):
        return [('model', str)]

class ModelStep(NameParser):
    def __init__(self):
        self.rgx = re.compile("^(.*)-global_step(\d+)$")
        
    def parse(self, run_id):
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

class Combiner(NameParser):
    def __init__(parser_list):
        self.parser_list = parser_list

    def parse(self, run_id):
        for name_parser in self.parser_list:
            out = name_parser.parse(run_id)
            if out is not None:
                return out
        return None

    def columns(self):
        cols = []

        for name_parser in self.parser_list:
            cols.append(name_parser.columns())

        return list(itertools.chain.from_iterable(cols))
