import json

from lm_plot.eval.plot import _plot_one, _plot_multi, _data

class _LMEval:
    def __init__(self, df):
        self.df_ = df
    
    def to_feather(self, path):
        self.df_.to_feather(path)

    def plot(
        self,
        x,
        title_prefix=None,
        metric=None,
        legend=True,
        **axes,
    ):
        return _plot_one(
            self.df_,
            x=x,
            title_prefix=title_prefix,
            metric=metric,
            legend=legend,
            **axes,
        )

    def plot_multi(
        self,
        grid,
        x,
        title_prefix=None,
        metric=None,
        legend=True,
        **axes,
    ):
        return _plot_multi(
            self.df_,
            grid=grid,
            x=x,
            title_prefix=None,
            metric=None,
            legend=legend,
            **axes,
        )

    def data(self, x, title_prefix=None, metric=None, **axes):
        selected_df, _title, _display_metric, _hue = _data(
            self.df_,
            x,
            title_prefix,
            metric,
            **axes
        )

        return selected_df

    def raw(self):
        return self.df_

    def all(self, axis):
        return sorted(self.df_[axis].unique().tolist())
