import numpy as np
from scipy.optimize import differential_evolution,minimize
f=lambda x:(x[0]-2)**2+3*(x[1]+1)**2+.1*np.sin(5*x[0]);g=differential_evolution(f,[(-5,5),(-5,5)],seed=42);l=minimize(f,g.x,method='BFGS');print(g.fun,l.fun,l.x)
