"""Problema da mochila binária usando OR-Tools."""
from ortools.linear_solver import pywraplp
values=[20,30,35,12,3]
weights=[2,5,7,3,1]
capacity=10
s=pywraplp.Solver.CreateSolver("SCIP")
x=[s.BoolVar(f"x{i}") for i in range(len(values))]
s.Add(sum(weights[i]*x[i] for i in range(len(x)))<=capacity)
s.Maximize(sum(values[i]*x[i] for i in range(len(x))))
s.Solve()
print([i for i,v in enumerate(x) if v.solution_value()>0.5], s.Objective().Value())
