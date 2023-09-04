N,M,V = map(int,input().split())
lst = [[] for _ in range(N+1)]
for i in range(M):
    s,e = map(int,input().split())
    lst[s].append(e)
    lst[e].append(s)
visited = [0]*(N+1)
for i in range(N):
    lst[i].sort()
def dfs(now):
    for i in lst[now]:
        if visited[i]!=1:
            print(i,end = ' ')
            visited[i]=1
            dfs(i)
print(V, end=' ')
dfs(V)