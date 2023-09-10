from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global Max
    while q:
        x,level = q.popleft()
        if x == m:
            result.append(level)
            used[x]=0
        for i in (x-1,2*x,x+1):
            if 0<=i<=100000:
                if used[i]==0:
                    used[i]=1
                    q.append([i,level+1])
                    dist.append(i)



q= deque()
Max = 0
n,m = map(int,input().split())
used = [0]*100001
used[n]=1
dist,result = [],[]

q.append([n,0])
bfs()

print(min(result))
