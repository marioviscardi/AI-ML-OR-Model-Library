from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
X,_=make_blobs(n_samples=500,centers=4,random_state=42)
m=KMeans(n_clusters=4,n_init="auto",random_state=42).fit(X)
print(m.cluster_centers_)
