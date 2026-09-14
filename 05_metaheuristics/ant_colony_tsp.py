"""ACO compacto para TSP."""
import numpy as np
rng=np.random.default_rng(42)
pts=rng.random((12,2))
D=np.linalg.norm(pts[:,None,:]-pts[None,:,:],axis=2)+np.eye(len(pts))*1e9
tau=np.ones_like(D)
alpha,beta,rho=1.0,3.0,.3
best=(1e9,None)
for _ in range(120):
    tours=[]
    for _a in range(40):
        un=set(range(1,len(pts))); tour=[0]
        while un:
            i=tour[-1]
            cand=np.array(list(un))
            desir=(tau[i,cand]**alpha)*((1/D[i,cand])**beta)
            j=rng.choice(cand,p=desir/desir.sum())
            tour.append(int(j)); un.remove(int(j))
        tour.append(0)
        L=sum(D[tour[k],tour[k+1]] for k in range(len(tour)-1))
        tours.append((L,tour))
        if L<best[0]: best=(L,tour)
    tau*=1-rho
    for L,t in tours:
        for a,b in zip(t[:-1],t[1:]): tau[a,b]+=1/L
print(best)
