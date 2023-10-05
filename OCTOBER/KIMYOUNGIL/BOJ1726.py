from collections import deque

def bfs(a, b, c):
    diry = [0, 0, 1, -1]
    dirx = [1, -1, 0, 0]
    change = [[2, 3], [2, 3], [0, 1], [0, 1]]
    q = deque([[a, b, c, 0]])
    visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    while q:
        y, x, dir, cnt = q.popleft()
        if y == gy - 1 and x == gx - 1 and dir == gd - 1:
            return print(cnt)

        for i in range(1, 4):
            dy = y + diry[dir] * i
            dx = x + dirx[dir] * i
            dr = dir
            if dy < 0 or dx < 0 or dy > n - 1 or dx > m - 1: continue
            if arr[dy][dx] == 1: break
            if arr[dy][dx] == 0 and visited[dy][dx][dr] == 0:
                visited[dy][dx][dr] = 1
                q.append([dy, dx, dir, cnt + 1])

        for i in change[dir]:
            if visited[y][x][i] == 0:
                visited[y][x][i] = 1
                q.append([y, x, i, cnt + 1])

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, e, d = map(int, input().split())
gy, gx, gd = map(int, input().split())
bfs(s - 1, e - 1, d - 1)