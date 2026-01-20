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
        vol_df = pd.DataFrame({'ticker': self.assets, 'volatility': vol.values})
        self.kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
        labels = self.kmeans.fit_predict(vol_df[['volatility']])
        vol_df['risk_cluster'] = labels
        self.vol_df = vol_df

    def get_all_clusters(self):
        means = self.vol_df.groupby('risk_cluster')['volatility'].mean().sort_values().index.tolist()
        cluster_map = dict(zip(means, ['Safe', 'Medium', 'Risky']))
        return [(t, cluster_map[self.vol_df.loc[self.vol_df['ticker'] == t, 'risk_cluster'].values[0]]) for t in self.assets]
