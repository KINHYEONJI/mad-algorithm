import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
inf = int(12e12)

m, n = map(int, input().split())
arr = [ list(map(int, input())) for _ in range(n)]
used = [[inf] * m for _ in range(n)]

q = deque()
q.append((0,0))
used[0][0] = 0
while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if used[nx][ny] == inf:
                if arr[nx][ny] == 0:
                    used[nx][ny] = used[x][y]
                    q.appendleft((nx, ny))
                else:
                    used[nx][ny] = used[x][y] + 1
                    q.append((nx, ny))

print(used[n - 1][m - 1])