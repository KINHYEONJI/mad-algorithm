import sys
from collections import deque
input = sys.stdin.readline
def bfs():
    global m,ct,v_ct
    num=0
    while q:
        x = q.popleft()
        if x == m:
            ct+=1
            v_ct = visited[x]
            continue

        for i in (x-1,x+1,x*2):
            if 0<=i<=100000 and (visited[i]==0 or visited[i]==visited[x]+1):
                visited[i] = visited[x]+1
                q.append(i)

n,m = map(int,input().split())
num,ct,v_ct=0,0,0
q = deque()
q.append(n)
visited = [0]*100001
bfs()
print(v_ct)
print(ct)
