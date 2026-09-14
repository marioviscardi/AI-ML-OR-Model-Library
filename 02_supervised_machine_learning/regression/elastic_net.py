from sklearn.datasets import make_regression
from sklearn.linear_model import ElasticNet
X,y=make_regression(n_samples=500,n_features=12,noise=12,random_state=42)
m=ElasticNet(alpha=.01,l1_ratio=.5).fit(X,y)
print(m.score(X,y))
