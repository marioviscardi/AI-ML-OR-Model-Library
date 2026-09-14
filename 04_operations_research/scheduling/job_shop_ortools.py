"""Job-shop pequeno com CP-SAT."""
from ortools.sat.python import cp_model

jobs=[[(0,3),(1,2)],[(1,2),(0,4)]]
m=cp_model.CpModel()
horizon=sum(t for job in jobs for _,t in job)
machine_intervals={0:[],1:[]}
ends={}
for j,job in enumerate(jobs):
    prev=None
    for k,(machine,dur) in enumerate(job):
        s=m.NewIntVar(0,horizon,f"s_{j}_{k}")
        e=m.NewIntVar(0,horizon,f"e_{j}_{k}")
        itv=m.NewIntervalVar(s,dur,e,f"i_{j}_{k}")
        machine_intervals[machine].append(itv)
        if prev is not None: m.Add(s>=prev)
        prev=e
    ends[j]=prev
for itvs in machine_intervals.values(): m.AddNoOverlap(itvs)
makespan=m.NewIntVar(0,horizon,"makespan")
m.AddMaxEquality(makespan,list(ends.values()))
m.Minimize(makespan)
solver=cp_model.CpSolver(); solver.Solve(m)
print("makespan",solver.Value(makespan))
