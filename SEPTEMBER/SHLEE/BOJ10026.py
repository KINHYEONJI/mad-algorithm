from collections import deque

def bfs(y, x):
    q = deque()
    q.append([y, x])
    used[y][x] = 1

    while q:
        yy, xx = q.popleft()
        dty = [-1, 0, 1, 0]
        dtx = [0, 1, 0, -1]
        for i in range(4):
            dy = yy + dty[i]
            dx = xx + dtx[i]
            if dx < 0 or dy < 0 or dx > N - 1 or dy > N - 1: continue
            if used[dy][dx] == 1: continue
            if arr[dy][dx] == arr[yy][xx]:
                used[dy][dx] = 1
                q.append([dy, dx])


N = int(input())
arr = [list(input()) for _ in range(N)]
used = [[0] * N for _ in range(N)]
cntn, cnty = 0, 0

# 적록색맹이 아닌 경우
for i in range(N):
    for j in range(N):
        if used[i][j] == 0:
            bfs(i, j)
            cntn += 1

# 적록색맹인 경우
used = [[0] * N for _ in range(N)]      # used 초기화
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if used[i][j] == 0:
            bfs(i, j)
            cnty += 1

print(cntn,cnty)