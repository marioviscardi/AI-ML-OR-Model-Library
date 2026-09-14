from scipy.optimize import basinhopping
f=lambda x:sum((v*v-1)**2 for v in x);r=basinhopping(f,[2,2,2],niter=100,seed=42);print(r.fun,r.x)
