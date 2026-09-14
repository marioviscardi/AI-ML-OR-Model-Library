from scipy.optimize import minimize
f=lambda x:sum(v*v for v in x);r=minimize(f,[3,2,-4],method='Nelder-Mead');print(r.fun,r.x)
