import numpy as np
from scipy.optimize import linprog
c=np.array([[2,3,1],[5,4,8]]); supply=[30,40]; demand=[20,30,20]; A=[]; b=[]
for i,s in enumerate(supply): row=np.zeros(c.size); row[i*3:(i+1)*3]=1; A.append(row); b.append(s)
Ae=[]; be=[]
for j,d in enumerate(demand): row=np.zeros(c.size); row[j::3]=1; Ae.append(row); be.append(d)
r=linprog(c.ravel(),A_ub=A,b_ub=b,A_eq=Ae,b_eq=be,bounds=(0,None),method='highs'); print(r.fun,r.x.reshape(c.shape))
