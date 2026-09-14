from sklearn.datasets import make_regression
from sklearn.svm import SVR
X,y=make_regression(n_samples=500,n_features=12,noise=12,random_state=42)
m=SVR(C=10).fit(X,y)
print(m.score(X,y))
