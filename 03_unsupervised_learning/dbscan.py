from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
X,_=make_moons(n_samples=500,noise=.06,random_state=42)
labels=DBSCAN(eps=.25,min_samples=5).fit_predict(StandardScaler().fit_transform(X))
print("clusters/noise:", sorted(set(labels)))
