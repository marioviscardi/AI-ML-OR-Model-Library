import numpy as np
r=np.random.default_rng(42);X=r.uniform(-5,5,(40,5));f=lambda x:(x*x).sum()
for t in range(200):
 X=X[np.argsort([f(x) for x in X])];a=2*(1-t/200);L=X[:3];Y=[]
 for x in X:
  Z=[]
  for l in L:
   r1,r2=r.random(2);A=2*a*r1-a;C=2*r2;Z.append(l-A*np.abs(C*l-x))
  Y.append(np.mean(Z,axis=0))
 X=np.array(Y)
b=min(X,key=f);print(f(b),b)
