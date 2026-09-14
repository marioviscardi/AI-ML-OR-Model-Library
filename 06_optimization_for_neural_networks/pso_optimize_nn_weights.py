"""Esqueleto conceitual: PSO para otimizar vetor de pesos de uma rede pequena."""
import numpy as np
rng=np.random.default_rng(42)
X=rng.normal(size=(120,2))
y=(X[:,0]+X[:,1]>0).astype(float)

def sigmoid(z): return 1/(1+np.exp(-z))

# rede 2 -> 3 -> 1; vetor = W1(6)+b1(3)+W2(3)+b2(1) = 13
def loss(theta):
    W1=theta[:6].reshape(2,3); b1=theta[6:9]
    W2=theta[9:12].reshape(3,1); b2=theta[12]
    h=np.tanh(X@W1+b1)
    p=sigmoid((h@W2).ravel()+b2)
    return -np.mean(y*np.log(p+1e-9)+(1-y)*np.log(1-p+1e-9))

n,d=50,13
pos=rng.normal(size=(n,d)); vel=np.zeros_like(pos)
pbest=pos.copy(); pval=np.array([loss(z) for z in pos])
gbest=pbest[pval.argmin()].copy()
for _ in range(250):
    r1,r2=rng.random((2,n,d))
    vel=.7*vel+1.4*r1*(pbest-pos)+1.4*r2*(gbest-pos)
    pos+=vel
    vals=np.array([loss(z) for z in pos])
    better=vals<pval
    pbest[better]=pos[better]; pval[better]=vals[better]
    gbest=pbest[pval.argmin()].copy()
print("best BCE:", loss(gbest))
