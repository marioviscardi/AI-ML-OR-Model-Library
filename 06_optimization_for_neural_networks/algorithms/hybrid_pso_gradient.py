import numpy as np
from scipy.optimize import minimize
r=np.random.default_rng(42);f=lambda x:np.sum(x*x)+.1*np.sum(np.sin(5*x));X=r.uniform(-5,5,(30,4));V=np.zeros_like(X);P=X.copy();F=np.array([f(x) for x in X]);G=P[F.argmin()].copy()
for _ in range(120):
 a,b=r.random((2,*X.shape));V=.7*V+1.4*a*(P-X)+1.4*b*(G-X);X+=V;Z=np.array([f(x) for x in X]);q=Z<F;P[q]=X[q];F[q]=Z[q];G=P[F.argmin()].copy()
l=minimize(f,G,method='BFGS');print(l.fun,l.x)
