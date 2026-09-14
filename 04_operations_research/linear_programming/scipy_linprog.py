"""Minimiza 3x + 2y sujeito a restrições lineares."""
from scipy.optimize import linprog
c=[3,2]
A=[[-1,-1],[-1,0],[0,-1]]
b=[-4,-1,-1]
res=linprog(c,A_ub=A,b_ub=b,bounds=[(0,None),(0,None)],method="highs")
print(res.x, res.fun)
