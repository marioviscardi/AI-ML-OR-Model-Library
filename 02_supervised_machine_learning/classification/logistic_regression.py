from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
X,y=load_breast_cancer(return_X_y=True); m=LogisticRegression(max_iter=1000).fit(X,y); print(m.score(X,y))
