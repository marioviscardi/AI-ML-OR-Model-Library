from sklearn.datasets import make_regression
from xgboost import XGBRegressor
X,y=make_regression(n_samples=500,n_features=12,noise=12,random_state=42); m=XGBRegressor(n_estimators=150,random_state=42).fit(X,y); print(m.score(X,y))
