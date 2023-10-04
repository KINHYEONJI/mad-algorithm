import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x):
    q = deque()
    q.append([y, x])
    size = 1
    arr[y][x] = 1

    while q:
        yy, xx = q.popleft()
        dty = [-1, 0, 1, 0]
        dtx = [0, 1, 0, -1]
        for i in range(4):
            dy = yy + dty[i]
            dx = xx + dtx[i]
            if dx < 0 or dy < 0 or dx > m - 1 or dy > n - 1: continue
            if arr[dy][dx] == 1: continue
            arr[dy][dx] = 1
            size += 1
            q.append([dy, dx])

    return size


m, n, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for _ in range(k):
    sr, sc, er, ec = map(int, input().split())
    for i in range(sr, er):
        for j in range(sc, ec):
            arr[i][j] = 1
cnt = 0
lst = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            cnt += 1
            ret = bfs(i, j)
            lst.append(ret)

print(cnt)
lst.sort()
print(*lst)