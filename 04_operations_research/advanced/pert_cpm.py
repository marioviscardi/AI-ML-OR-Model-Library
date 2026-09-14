import networkx as nx
G=nx.DiGraph(); [G.add_edge(a,b,duration=d) for a,b,d in [('S','A',3),('S','B',2),('A','C',4),('B','C',1),('C','T',5)]]; e={n:0 for n in G}
for u in nx.topological_sort(G):
 for v in G.successors(u):e[v]=max(e[v],e[u]+G[u][v]['duration'])
print(e)
