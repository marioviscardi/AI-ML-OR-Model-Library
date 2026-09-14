from sklearn.datasets import load_digits
import umap
X,_=load_digits(return_X_y=True); print(umap.UMAP(2,random_state=42).fit_transform(X).shape)
