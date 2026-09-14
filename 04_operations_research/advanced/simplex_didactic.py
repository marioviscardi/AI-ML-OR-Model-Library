import numpy as np
T=np.array([[1.,1,1,0,0,4],[1,0,0,1,0,2],[0,1,0,0,1,3],[-3,-2,0,0,0,0]])
while T[-1,:-1].min()<-1e-9:
 c=int(np.argmin(T[-1,:-1])); ratios=[T[i,-1]/T[i,c] if T[i,c]>1e-12 else np.inf for i in range(len(T)-1)]; r=int(np.argmin(ratios)); T[r]/=T[r,c]
 for i in range(len(T)):
  if i!=r:T[i]-=T[i,c]*T[r]
print(T,'opt=',T[-1,-1])
