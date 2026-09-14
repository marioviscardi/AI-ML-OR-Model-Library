v=[20,30,35,12,3]; w=[2,5,7,3,1]; C=10; best=(0,None)
def dfs(i,W,V,s):
 global best
 if W>C:return
 if i==len(v):
  if V>best[0]:best=(V,s)
  return
 dfs(i+1,W,V,s+[0]); dfs(i+1,W+w[i],V+v[i],s+[1])
dfs(0,0,0,[]); print(best)
