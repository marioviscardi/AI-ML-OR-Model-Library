from sklearn.datasets import load_breast_cancer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
X,y=load_breast_cancer(return_X_y=True); m=LinearDiscriminantAnalysis().fit(X,y); print(m.score(X,y))
