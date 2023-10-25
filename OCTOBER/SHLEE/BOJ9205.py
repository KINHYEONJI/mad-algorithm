import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append([hx, hy])

    while q:
        x, y = q.popleft()
        if abs(x - fx) + abs(y - fy) <= 1000:
            print('happy')
            return
        for i in range(n):
            if used[i] == 0:
                cx, cy = arr[i]
                if abs(x - cx) + abs(y - cy) <= 1000:
                    used[i] = 1
                    q.append([cx, cy])

    print('sad')
    return


T = int(input())
for _ in range(T):
    n = int(input())
    hx, hy = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    fx, fy = map(int, input().split())
    used = [0 for _ in range(n + 1)]
    bfs()