"""Particle Swarm Optimization para minimizar Sphere."""
import numpy as np
rng=np.random.default_rng(42)
n,d=40,5
x=rng.uniform(-5,5,(n,d)); v=np.zeros_like(x)
p=x.copy(); pf=(p*p).sum(1)
g=p[pf.argmin()].copy()
for _ in range(300):
    r1,r2=rng.random((2,n,d))
    v=.7*v+1.5*r1*(p-x)+1.5*r2*(g-x)
    x+=v
    fx=(x*x).sum(1)
    better=fx<pf
    p[better]=x[better]; pf[better]=fx[better]
    g=p[pf.argmin()].copy()
print((g*g).sum(),g)
