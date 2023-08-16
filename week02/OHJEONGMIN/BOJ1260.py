from collections import deque
N,M,V = map(int,input().split())
lst = [[] for _ in range(N+1)]
for i in range(M):
    s,e = map(int,input().split())
    lst[s].append(e)
    lst[e].append(s)
visited1 = [0]*(N+1)
visited2 = [0]*(N+1)
for i in range(1,N+1):
    lst[i].sort()
def dfs(now):
    print(now, end=' ')
    for i in lst[now]:
        if visited1[i] == 0:
            visited1[i]=1
            dfs(i)
visited1[V]=1
dfs(V)
print()

def bfs(now):
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in lst[now]:
            if visited2[i]==0:
                q.append(i)
                visited2[i]=1

visited2[V]=1
bfs(V)