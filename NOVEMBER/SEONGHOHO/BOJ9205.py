import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        nx, ny = q.popleft()
        if abs(nx - fx) + abs(ny - fy) <= 1000:
            print('happy')
            return
        for i in range(n):
            if used[i] == 1: continue
            if abs(nx - lst[i][0]) + abs(ny - lst[i][1]) <= 1000:
                used[i] = 1
                q.append([lst[i][0], lst[i][1]])

    print('sad')
    return


t = int(input())
for _ in range(t):
    n = int(input())

    sx, sy = map(int, input().split())
    lst = [list(map(int, input().strip().split())) for _ in range(n)]
    fx, fy = map(int, input().split())
    used = [0 for _ in range(n + 1)]

    bfs(sx, sy)
