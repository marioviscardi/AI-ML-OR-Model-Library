from sklearn.datasets import load_digits
from sklearn.decomposition import FastICA
X,_=load_digits(return_X_y=True); print(FastICA(n_components=20,random_state=42,max_iter=1000).fit_transform(X).shape)
