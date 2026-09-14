from sklearn.datasets import make_moons
from sklearn.cluster import SpectralClustering
X,_=make_moons(n_samples=400,noise=.06,random_state=42); print(SpectralClustering(2,affinity='nearest_neighbors',random_state=42).fit_predict(X)[:20])
