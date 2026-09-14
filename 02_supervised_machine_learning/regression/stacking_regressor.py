from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor,StackingRegressor
from sklearn.linear_model import Ridge
from sklearn.svm import SVR
X,y=make_regression(n_samples=500,n_features=12,noise=12,random_state=42); m=StackingRegressor([('rf',RandomForestRegressor(n_estimators=80,random_state=42)),('svr',SVR())],final_estimator=Ridge()).fit(X,y); print(m.score(X,y))
