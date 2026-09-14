from sklearn.datasets import make_moons
from sklearn.decomposition import KernelPCA
X,_=make_moons(n_samples=400,noise=.05,random_state=42); print(KernelPCA(2,kernel='rbf',gamma=15).fit_transform(X).shape)
