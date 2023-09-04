from collections import deque


def bfs(y, x):
    q = deque()
    q.append([y, x])
    arr[y][x] = 0
    size = 1
    while q:
        yy, xx = q.popleft()
        dty = [-1, 0, 1, 0]
        dtx = [0, 1, 0, -1]
        for i in range(4):
            dy = yy + dty[i]
            dx = xx + dtx[i]
            if dx < 0 or dy < 0 or dy > n - 1 or dx > m - 1: continue
            if arr[dy][dx] == 0: continue
            arr[dy][dx] = 0
            q.append([dy, dx])
            size += 1

    return size


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
mx = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt += 1
            ret = bfs(i, j)
            if ret > mx:
                mx = ret

print(cnt)
print(mx)