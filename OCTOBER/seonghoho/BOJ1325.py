import sys
from collections import deque

def bfs(n):
    q = deque([n])
    cnt = 1
    visited = [False] * (N+1)
    visited[n] = True
    while q:
        now = q.popleft()
        for j in com[now]:
            if not visited[j]:
                visited[j] = True
                q.append(j)
                cnt += 1
    return cnt

N, M = map(int, sys.stdin.readline().split())
com = [[] for _ in range(N + 1)]
Max = -21e8
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    com[b].append(a)

res = []
for i in range(1, N+1):
    res.append(bfs(i))

Max = max(res)
for i in range(len(res)):
    if Max == res[i]:
        print(i+1, end=' ')
