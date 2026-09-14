import numpy as np
r=np.random.default_rng(42);X=r.uniform(-5,5,(30,5));f=lambda x:(x*x).sum()
for _ in range(500):
 i,j=r.integers(30,size=2);y=X[i]+.1*r.standard_cauchy(5);X[j]=y if f(y)<f(X[j]) else X[j]
b=min(X,key=f);print(f(b),b)
