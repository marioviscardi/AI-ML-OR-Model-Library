from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
import hdbscan
X,_=make_moons(n_samples=600,noise=.06,random_state=42); print(sorted(set(hdbscan.HDBSCAN(min_cluster_size=20).fit_predict(StandardScaler().fit_transform(X)))))
