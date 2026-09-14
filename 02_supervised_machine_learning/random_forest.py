from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
X,y=load_breast_cancer(return_X_y=True)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
m=RandomForestClassifier(n_estimators=300,random_state=42,n_jobs=-1).fit(Xtr,ytr)
print("accuracy",accuracy_score(yte,m.predict(Xte)))
