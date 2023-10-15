from collections import deque
import sys

input = sys.stdin.readline

dry = [0, 0, 1, -1]
drx = [1, -1, 0, 0]
direct_d = [[2, 3], [2, 3], [0, 1], [0, 1]]


def bfs():
    global used
    q = deque()
    q.append([sy - 1, sx - 1, sd - 1, 0])
    used = [[[0] * 4 for _ in range(N)] for _ in range(M)]
    used[sy - 1][sx - 1][sd - 1] = 1
    while q:
        nowy, nowx, nowd, cnt = q.popleft()

        if nowy == ay - 1 and nowx == ax - 1 and nowd == ad - 1:
            return cnt

        for i in range(1, 4):
            dy = nowy + dry[nowd] * i
            dx = nowx + drx[nowd] * i
            dd = nowd

            if dy < 0 or dy > M - 1 or dx < 0 or dx > N - 1: break
            if lst[dy][dx] == 1: break
            if used[dy][dx][dd] == 1: continue
            used[dy][dx][dd] = 1
            q.append([dy, dx, dd, cnt + 1])

        for j in direct_d[nowd]:
            if used[nowy][nowx][j] == 1: continue
            used[nowy][nowx][j] = 1
            q.append([nowy, nowx, j, cnt + 1])


M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
sy, sx, sd = map(int, input().split())
ay, ax, ad = map(int, input().split())

print(bfs())
