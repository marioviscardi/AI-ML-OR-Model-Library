from sklearn.datasets import load_breast_cancer
from xgboost import XGBClassifier
X,y=load_breast_cancer(return_X_y=True); m=XGBClassifier(n_estimators=150,random_state=42).fit(X,y); print(m.score(X,y))
