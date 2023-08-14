from collections import deque

n,m,v = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)
    arr[s].sort()
    arr[e].sort()

used = [0]*(n+1)
def dfs(x):
    print(x,end=" ")
    for i in arr[x]:
        if used[i] == 0:
            used[i] = 1
            dfs(i)

used[v] = 1
dfs(v)
print()

used1 = [0]*(n+1)
def bfs(x):
    q = deque()
    q.append(x)
    while q:
        a = q.popleft()
        print(a,end=" ")
        for i in arr[a]:
            if used1[i] == 0:
                used1[i] = 1
                q.append(i)

used1[v] = 1
bfs(v)