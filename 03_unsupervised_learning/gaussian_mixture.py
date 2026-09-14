from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture
X,_=make_blobs(n_samples=500,centers=3,cluster_std=[1.0,2.0,.5],random_state=42)
m=GaussianMixture(n_components=3,random_state=42).fit(X)
print(m.predict_proba(X[:5]))
