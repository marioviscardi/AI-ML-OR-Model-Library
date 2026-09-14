"""TSP didático por busca exaustiva. Use apenas para poucos nós."""
from itertools import permutations
import math
pts=[(0,0),(1,5),(5,2),(6,6),(8,3)]
def d(a,b): return math.dist(pts[a],pts[b])
best=None
for p in permutations(range(1,len(pts))):
    route=(0,)+p+(0,)
    cost=sum(d(route[i],route[i+1]) for i in range(len(route)-1))
    if best is None or cost<best[0]: best=(cost,route)
print(best)
