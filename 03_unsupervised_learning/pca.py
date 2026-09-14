from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
X,_=load_digits(return_X_y=True)
Z=PCA(n_components=2,random_state=42).fit_transform(StandardScaler().fit_transform(X))
print(Z.shape)
