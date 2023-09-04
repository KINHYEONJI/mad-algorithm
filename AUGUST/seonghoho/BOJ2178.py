from collections import deque

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
cnt = 1
used = [[0] * M for _ in range(N)]


def bfs(sty, stx, edy, edx):
    q = deque()
    q.append([sty, stx, 1])

    while q:
        nowy, nowx, level = q.popleft()
        dry = [0, 0, -1, 1]
        drx = [-1, 1, 0, 0]
        for i in range(4):
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if dy < 0 or dx < 0 or dy > N - 1 or dx > M - 1: continue
            if used[dy][dx] == 1: continue
            if lst[dy][dx] == '0': continue

            used[dy][dx] = 1
            q.append((dy, dx, level + 1))

            if dy == edy and dx == edx:
                return level + 1


used[0][0] = 1
n = bfs(0, 0, N-1, M-1)
print(n)