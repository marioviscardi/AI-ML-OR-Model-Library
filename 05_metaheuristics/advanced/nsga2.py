from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.problems import get_problem
from pymoo.optimize import minimize
r=minimize(get_problem('zdt1'),NSGA2(pop_size=80),('n_gen',100),seed=42,verbose=False); print(r.F[:5])
