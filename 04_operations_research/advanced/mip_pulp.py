import pulp as pl
m=pl.LpProblem('mip',pl.LpMaximize); x=pl.LpVariable('x',0,cat='Integer'); y=pl.LpVariable('y',0,cat='Integer'); m+=5*x+4*y; m+=6*x+4*y<=24; m+=x+2*y<=6; m.solve(pl.PULP_CBC_CMD(msg=False)); print(x.value(),y.value(),pl.value(m.objective))
