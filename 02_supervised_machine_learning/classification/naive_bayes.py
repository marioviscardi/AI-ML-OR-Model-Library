from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
X,y=load_breast_cancer(return_X_y=True); m=GaussianNB().fit(X,y); print(m.score(X,y))
