from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
X,_=load_digits(return_X_y=True); print(TSNE(2,perplexity=30,random_state=42,init='pca').fit_transform(X[:800]).shape)
