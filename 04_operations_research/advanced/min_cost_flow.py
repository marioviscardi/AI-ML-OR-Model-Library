import networkx as nx
G=nx.DiGraph(); G.add_node('s',demand=-5);G.add_node('a',demand=0);G.add_node('t',demand=5);G.add_edge('s','a',capacity=5,weight=2);G.add_edge('a','t',capacity=5,weight=1);print(nx.min_cost_flow_cost(G),nx.min_cost_flow(G))
