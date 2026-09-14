"""Differential Evolution via SciPy."""
from scipy.optimize import differential_evolution
def f(x): return sum(v*v for v in x)
res=differential_evolution(f,[(-5,5)]*5,seed=42)
print(res.fun,res.x)
