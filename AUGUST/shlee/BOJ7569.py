from collections import deque


def bfs():
    dty = [0, 0, -1, 0, 1, 0]
    dtx = [0, 0, 0, 1, 0, -1]
    dtz = [1, -1, 0, 0, 0, 0]
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            dy = y + dty[i]
            dx = x + dtx[i]
            dz = z + dtz[i]
            if dx < 0 or dx > M - 1 or dy < 0 or dy > N - 1 or dz < 0 or dz > H - 1: continue
            if arr[dz][dy][dx] == 0:
                arr[dz][dy][dx] = arr[z][y][x] + 1
                q.append([dz, dy, dx])


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()     # 원소가 1인 값들을 미리 q에 넣어 놓고 시작.
ans = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                q.append([k, i, j])

bfs()

flag = 0
for i in arr:
    for j in i:
        for k in j:
            if k == 0:
                flag = 1
                break

if flag:
    print(-1)
else:
    mx = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                mx = max(mx, arr[i][j][k])
    print(mx - 1)