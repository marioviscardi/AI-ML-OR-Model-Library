from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
X,y=make_regression(n_samples=500,n_features=12,noise=12,random_state=42)
m=Ridge(alpha=1.0).fit(X,y)
print(m.score(X,y))
