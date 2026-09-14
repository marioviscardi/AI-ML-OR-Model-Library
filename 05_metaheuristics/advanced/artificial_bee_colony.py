import numpy as np
r=np.random.default_rng(42);X=r.uniform(-5,5,(30,5));F=(X*X).sum(1)
for _ in range(500):
 for i in range(30):
  k=r.choice([j for j in range(30) if j!=i]);V=X[i]+r.uniform(-1,1,5)*(X[i]-X[k]);v=(V*V).sum();
  if v<F[i]:X[i],F[i]=V,v
print(F.min(),X[F.argmin()])
