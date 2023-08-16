from collections import deque
N, M , V = map(int, input().split())
arr = [[] for _ in range(M)]
for i in range(M):
    st, ed = map(int, input().split())
    arr[st].append(ed)
    arr[ed].append(st)
used1 = [0] * (N+1)

def dfs(now):
    print(now, end = ' ')
    for i in arr[now]:
        if used1[i] == 0:
            used1[i] = 1
            dfs(i)

used1[V] = 1
dfs(V)
print()
used2 = [0] * (N+1)

def bfs(now):
    q=deque()
    q.append(now)
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in arr[now]:
            if used2[i] ==0 :
                q.append(i)
                used2[i] = 1
used2[V]=1
bfs(V)


