import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x):
    global used
    q = deque()
    q.append([y, x])
    dty = [-1, 0, 1, 0]
    dtx = [0, 1, 0, -1]
    used[y][x] = 1
    while q:
        yy, xx = q.popleft()
        for i in range(4):
            dy, dx = yy + dty[i], xx + dtx[i]
            if dx < 0 or dy < 0 or dx > N - 1 or dy > N - 1: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append([dy, dx])

    return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
maxx = max(map(max, arr))
minn = min(map(min, arr))

ans = 1
while minn < maxx:
    cnt = 0
    used = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= minn:
                used[i][j] = 1
    for i in range(N):
        for j in range(N):
            if used[i][j] == 0:
                bfs(i, j)
                cnt += 1
    ans = max(ans, cnt)
    minn += 1

print(ans)