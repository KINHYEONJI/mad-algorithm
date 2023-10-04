import math
from collections import deque
def bfs():
    global used,m
    while q:
        x,cnt = q.popleft()
        if x==m:
            return cnt
        for i in range(4):
            for j in range(10):
                new_x = list(str(x))
                new_x[i] = str(j)
                a =''.join(new_x)
                if int(a)>=1000 and used[int(a)]==0 and visited[int(a)]==0:
                    visited[int(a)]=1
                    q.append([int(a),cnt+1])
    return -1

for i in range(int(input())):
    used = [0]*10000
    used[0],used[1]=1,1
    n,m = map(int,input().split())
    visited = [0]*10000
    for i in range(2,100):
        if used[i]==1:
            continue
        for k in range(i+i,10000,i):
            used[k]=1
    q = deque()
    q.append([n,0])
    ret = bfs()
    if ret==-1:
        print('Impossible')
    else:
        print(ret)


