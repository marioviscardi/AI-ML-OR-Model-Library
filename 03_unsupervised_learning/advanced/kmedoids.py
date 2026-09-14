from sklearn.datasets import make_blobs
from sklearn_extra.cluster import KMedoids
X,_=make_blobs(n_samples=300,centers=3,random_state=42); m=KMedoids(3,random_state=42).fit(X); print(m.medoid_indices_)
