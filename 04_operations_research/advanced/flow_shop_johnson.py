jobs={'J1':(3,6),'J2':(8,4),'J3':(5,7),'J4':(2,9)}; L=[];R=[]; q=dict(jobs)
while q:
 j=min(q,key=lambda k:min(q[k])); a,b=q.pop(j); (L if a<=b else R).append(j)
print(L+R[::-1])
