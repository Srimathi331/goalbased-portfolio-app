import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

class AssetClusterer:
    def __init__(self, returns_df):
        self.assets = returns_df.columns.tolist()
        self.returns_df = returns_df
        self.labels = None
        self._fit_cluster_model()

    def _fit_cluster_model(self):
        vol = self.returns_df.std() * np.sqrt(252)

        vol_df = pd.DataFrame({
            'ticker': self.assets,
            'volatility': vol.values
        })

        # ✅ FIX: remove NaN volatility rows (important)
        vol_df = vol_df.dropna(subset=['volatility'])

        # if less than 3 tickers exist, KMeans cannot work
        if len(vol_df) < 3:
            self.vol_df = vol_df
            return

        self.kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
        labels = self.kmeans.fit_predict(vol_df[['volatility']])

        vol_df['risk_cluster'] = labels
        self.vol_df = vol_df

    def get_all_clusters(self):
        # if clustering did not happen
        if 'risk_cluster' not in self.vol_df.columns:
            return [(t, "Unknown") for t in self.vol_df['ticker'].tolist()]

        means = (
            self.vol_df.groupby('risk_cluster')['volatility']
            .mean()
            .sort_values()
            .index
            .tolist()
        )

        cluster_map = dict(zip(means, ['Safe', 'Medium', 'Risky']))

        return [
            (row['ticker'], cluster_map[row['risk_cluster']])
            for _, row in self.vol_df.iterrows()
        ]
