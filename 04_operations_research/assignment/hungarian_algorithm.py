"""Problema de atribuição pelo algoritmo Húngaro."""
import numpy as np
from scipy.optimize import linear_sum_assignment
cost=np.array([[9,2,7],[6,4,3],[5,8,1]])
r,c=linear_sum_assignment(cost)
print(list(zip(r,c)), "custo=",cost[r,c].sum())
