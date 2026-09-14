import random
random.seed(42);f=lambda x:sum(v*v for v in x);H=[[random.uniform(-5,5) for _ in range(5)] for _ in range(20)]
for _ in range(3000):
 x=[(random.choice(H)[j] if random.random()<.9 else random.uniform(-5,5)) for j in range(5)];x=[v+random.uniform(-.1,.1) if random.random()<.3 else v for v in x];k=max(range(len(H)),key=lambda i:f(H[i]));H[k]=x if f(x)<f(H[k]) else H[k]
b=min(H,key=f);print(f(b),b)
