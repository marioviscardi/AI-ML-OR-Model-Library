"""Caminho mínimo de Dijkstra."""
import heapq
g={0:[(1,4),(2,1)],1:[(3,1)],2:[(1,2),(3,5)],3:[]}
src=0
dist={v:float("inf") for v in g}; dist[src]=0
pq=[(0,src)]
while pq:
    d,u=heapq.heappop(pq)
    if d!=dist[u]: continue
    for v,w in g[u]:
        nd=d+w
        if nd<dist[v]:
            dist[v]=nd; heapq.heappush(pq,(nd,v))
print(dist)
