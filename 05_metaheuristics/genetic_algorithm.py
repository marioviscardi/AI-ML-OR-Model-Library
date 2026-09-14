"""Algoritmo Genético simples para minimizar Sphere."""
import random
random.seed(42)

def f(x): return sum(v*v for v in x)
pop=[[random.uniform(-5,5) for _ in range(5)] for _ in range(80)]

for gen in range(150):
    pop.sort(key=f)
    elite=pop[:10]
    new=elite[:]
    while len(new)<80:
        a,b=random.sample(pop[:40],2)
        child=[(x+y)/2 for x,y in zip(a,b)]
        child=[v+random.gauss(0,.15) if random.random()<.2 else v for v in child]
        new.append(child)
    pop=new
print(f(pop[0]), pop[0])
