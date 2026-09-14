from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
X,y=load_iris(return_X_y=True)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
m=make_pipeline(StandardScaler(),SVC(kernel="rbf",probability=True)).fit(Xtr,ytr)
print("accuracy",m.score(Xte,yte))
