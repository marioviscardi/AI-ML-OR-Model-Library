from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
X,_=make_blobs(n_samples=300,centers=3,random_state=42)
labels=AgglomerativeClustering(n_clusters=3,linkage="ward").fit_predict(X)
print(labels[:20])
