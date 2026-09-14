from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.problems import get_problem
from pymoo.optimize import minimize
from pymoo.util.ref_dirs import get_reference_directions
d=get_reference_directions('das-dennis',3,n_partitions=8);r=minimize(get_problem('dtlz2',n_var=12,n_obj=3),NSGA3(pop_size=len(d),ref_dirs=d),('n_gen',120),seed=42,verbose=False);print(r.F[:5])
