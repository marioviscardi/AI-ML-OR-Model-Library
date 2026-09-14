from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import AdaBoostClassifier
X,y=load_breast_cancer(return_X_y=True); m=AdaBoostClassifier(n_estimators=150,random_state=42).fit(X,y); print(m.score(X,y))
