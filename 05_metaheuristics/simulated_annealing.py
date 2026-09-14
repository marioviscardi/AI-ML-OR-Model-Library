"""Simulated Annealing para minimizar Sphere."""
import random, math
random.seed(42)
def f(x): return sum(v*v for v in x)
x=[random.uniform(-5,5) for _ in range(5)]
T=10.0
for _ in range(20000):
    y=[v+random.gauss(0,.2) for v in x]
    delta=f(y)-f(x)
    if delta<0 or random.random()<math.exp(-delta/T): x=y
    T*=.9995
print(f(x),x)
