f,s,g,u,d = map(int,input().split())
from collections import deque


v=[0] * (f+1)

def bfs(s):
    q=deque()
    q.append(s)
    v[s]=1
    v[0]=1
    while q:
        s=q.popleft()
        for i in [u,-d]:
            x=s+i
            if 0 <x <=f and v[x] ==0:
                v[x]=v[s]+1
                q.append(x)
                
    

bfs(s)

if v[g] == 0:
    print('use the stairs')
else:
    print(v[g]-1)