from sklearn.datasets import make_regression
from catboost import CatBoostRegressor
X,y=make_regression(n_samples=500,n_features=12,noise=12,random_state=42); m=CatBoostRegressor(iterations=150,verbose=False,random_seed=42).fit(X,y); print(m.score(X,y))
