"""
DFS와 BFS로 탐색한 결과 출력
"""
n, m, start = map(int, input().split())
lst = [[] for _ in range(n + 1)]
for i in range(m):
    s, e = map(int, input().split())
    lst[s].append(e)
    lst[e].append(s)

# 리스트 내부의 리스트 정렬
for i in range(1, n + 1):
    lst[i].sort()

# DFS 탐색 순서
used = [0] * (n + 1)


def dfs(now):
    print(now, end=' ')
    for i in lst[now]:
        if used[i] == 1: continue
        used[i] = 1
        dfs(i)


used[start] = 1
dfs(start)

# BFS 탐색 순서
from collections import deque

used = [0] * (n + 1)
ans = []


def bfs(now):
    q = deque()
    q.append(now)

    while q:
        n = q.popleft()
        ans.append(n)

        for i in lst[n]:
            if used[i] == 1:
                continue
            used[i] = 1
            q.append(i)


used[start] = 1
bfs(start)
print()
print(*ans)
