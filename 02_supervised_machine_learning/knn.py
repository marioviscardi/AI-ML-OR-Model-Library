from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
X,y=load_iris(return_X_y=True)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
m=make_pipeline(StandardScaler(),KNeighborsClassifier(n_neighbors=5)).fit(Xtr,ytr)
print("accuracy",m.score(Xte,yte))
