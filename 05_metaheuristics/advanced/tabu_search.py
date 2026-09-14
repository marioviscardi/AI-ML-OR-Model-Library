import random,math
random.seed(42);pts=[(random.random(),random.random()) for _ in range(12)]
def f(p):return sum(math.dist(pts[p[i]],pts[p[(i+1)%len(p)]]) for i in range(len(p)))
p=list(range(12));best=p[:];tab=[]
for _ in range(300):
 cand=[]
 for i in range(1,11):
  q=p[:];q[i],q[i+1]=q[i+1],q[i];mv=(q[i],q[i+1]);
  if mv not in tab:cand.append((f(q),q,mv))
 _,p,m=min(cand,key=lambda x:x[0]);tab=(tab+[m])[-15:];best=p[:] if f(p)<f(best) else best
print(f(best),best)
