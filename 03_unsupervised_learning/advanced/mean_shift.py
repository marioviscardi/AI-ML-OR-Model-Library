from sklearn.datasets import make_blobs
from sklearn.cluster import MeanShift
X,_=make_blobs(n_samples=400,centers=4,random_state=42); print(len(set(MeanShift().fit_predict(X))))
