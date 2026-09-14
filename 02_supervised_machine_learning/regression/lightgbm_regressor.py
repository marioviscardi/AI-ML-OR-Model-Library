from sklearn.datasets import make_regression
from lightgbm import LGBMRegressor
X,y=make_regression(n_samples=500,n_features=12,noise=12,random_state=42); m=LGBMRegressor(n_estimators=150,random_state=42,verbosity=-1).fit(X,y); print(m.score(X,y))
