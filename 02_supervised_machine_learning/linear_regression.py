from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
X,y=make_regression(n_samples=500,n_features=5,noise=10,random_state=42)
m=LinearRegression().fit(X,y)
print("R2",m.score(X,y))
