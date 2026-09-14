import numpy as np
from scipy.optimize import least_squares
x=np.linspace(0,2,30);y=2*np.exp(.7*x);r=least_squares(lambda p:p[0]*np.exp(p[1]*x)-y,[1,1],method='lm');print(r.x)
