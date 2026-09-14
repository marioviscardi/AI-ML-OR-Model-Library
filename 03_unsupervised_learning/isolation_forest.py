import numpy as np
from sklearn.ensemble import IsolationForest
rng=np.random.default_rng(42)
X=rng.normal(size=(500,2))
X[:10]+=8
m=IsolationForest(contamination=.02,random_state=42).fit(X)
print(m.predict(X)[:20])
