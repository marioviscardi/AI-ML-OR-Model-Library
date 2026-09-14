"""Gradiente descendente em f(x,y)=(x-3)^2 + 2(y+1)^2."""
import numpy as np
x=np.array([8.0,5.0])
eta=.1
for _ in range(100):
    grad=np.array([2*(x[0]-3),4*(x[1]+1)])
    x-=eta*grad
print(x)
