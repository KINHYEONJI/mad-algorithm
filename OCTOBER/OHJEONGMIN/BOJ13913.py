from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global Max
    while q:
        x,level,dist = q.popleft()
        if x == m:
            return level
        for i in (x-1,2*x,x+1):
            if 0<=i<=100000:
                if used[i]==0:
                    used[i]=1
                    if i==x-1:
                        q.append([i,level+1,1])
                        Dist[i].append(1)
                    elif i==2*x:
                        q.append([i,level+1,2])
                        Dist[i].append(2)
                    else:
                        q.append([i,level+1,3])
                        Dist[i].append(3)
q= deque()
Max = 0
n,m = map(int,input().split())
used = [0]*100001
visit_dist = [0]*100001
used[n]=1
Dist,result = [[] for _ in range(100001)],[m]
q.append([n,0,0])
ret =bfs()
for i in range(ret):
    if Dist[m][0] ==1:
        m+=1
        result.append(m)
    elif Dist[m][0] ==2:
        m//=2
        result.append(m)
    elif Dist[m][0]==3:
        m-=1
        result.append(m)
print(ret)
print(*result[::-1])
