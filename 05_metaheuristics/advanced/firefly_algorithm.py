import numpy as np
r=np.random.default_rng(42);X=r.uniform(-5,5,(30,5));f=lambda x:(x*x).sum()
for _ in range(150):
 for i in range(30):
  for j in range(30):
   if f(X[j])<f(X[i]):
    d=np.linalg.norm(X[i]-X[j]);X[i]+=np.exp(-d*d)*(X[j]-X[i])+.05*r.normal(size=5)
b=min(X,key=f);print(f(b),b)
