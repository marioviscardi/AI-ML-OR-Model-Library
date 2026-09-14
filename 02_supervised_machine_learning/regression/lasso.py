from sklearn.datasets import make_regression
from sklearn.linear_model import Lasso
X,y=make_regression(n_samples=500,n_features=12,noise=12,random_state=42)
m=Lasso(alpha=.1).fit(X,y)
print(m.score(X,y))
