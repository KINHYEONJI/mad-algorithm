import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

lst = []
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 1:
                lst.append([k, i, j])

dirz = [-1, 0, 0, 0, 0, 1]
diry = [0, -1, 0, 1, 0, 0]
dirx = [0, 0, 1, 0, -1, 0]

def bfs():
    q = deque()
    for i in lst:
        q.append(i)
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            dz = z + dirz[i]
            dy = y + diry[i]
            dx = x + dirx[i]
            if dz < 0 or dy < 0 or dx < 0 or dy > n - 1 or dx > m - 1 or dz > h - 1: continue
            if arr[dz][dy][dx] == 0:
                arr[dz][dy][dx] = arr[z][y][x] + 1
                q.append([dz, dy, dx])

bfs()

def abc():
    Max = -21e8
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if arr[k][i][j] == 0:
                    return print(-1)
                if arr[k][i][j] > Max:
                    Max = arr[k][i][j]

    return print(Max - 1)

abc()