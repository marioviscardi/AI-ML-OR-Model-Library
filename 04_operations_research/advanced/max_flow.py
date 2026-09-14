import networkx as nx
G=nx.DiGraph(); [G.add_edge(u,v,capacity=c) for u,v,c in [('s','a',10),('s','b',5),('a','t',10),('b','t',10)]]; print(nx.maximum_flow(G,'s','t'))
