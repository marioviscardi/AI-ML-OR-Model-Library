from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
X,y=make_regression(n_samples=500,n_features=12,noise=12,random_state=42)
m=RandomForestRegressor(n_estimators=200,random_state=42,n_jobs=-1).fit(X,y)
print(m.score(X,y))
