from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
X,y=load_iris(return_X_y=True)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
m=DecisionTreeClassifier(max_depth=4,random_state=42).fit(Xtr,ytr)
print("accuracy",accuracy_score(yte,m.predict(Xte)))
