import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, ConstantKernel
X=np.linspace(0,10,40)[:,None]
y=np.sin(X[:,0])+np.random.default_rng(42).normal(0,.1,len(X))
kernel=ConstantKernel(1.0)*RBF(1.0)+WhiteKernel(.1)
m=GaussianProcessRegressor(kernel=kernel,normalize_y=True,random_state=42).fit(X,y)
Xt=np.linspace(0,10,100)[:,None]
mean,std=m.predict(Xt,return_std=True)
print(mean[:5]); print(std[:5])
