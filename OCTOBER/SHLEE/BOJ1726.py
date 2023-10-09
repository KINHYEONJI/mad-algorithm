import sys

input = sys.stdin.readline
from collections import deque

# 동 서 남 북 (0,1,2,3)
dty = [0, 0, 1, -1]
dtx = [1, -1, 0, 0]
# (동 or 서 -> 남 or 북), (남 or 북 -> 동 or 서) 으로 방향 전환 가능.
change_d = [[2, 3], [2, 3], [0, 1], [0, 1]]


def bfs():
    q = deque()
    q.append([sy - 1, sx - 1, sd - 1, 0])  # 좌표, 방향, 움직인 횟수 -> 인덱스 차이
    used = [[[0] * 4 for _ in range(n)] for _ in range(m)]  # 3차원 방문표시 -> 방향까지 포함
    used[sy - 1][sx - 1][sd - 1] = 1
    while q:
        yy, xx, d, cnt = q.popleft()
        # 도착지점에 도달한 경우
        if (yy, xx, d) == (ey - 1, ex - 1, ed - 1):
            return cnt
        # 1~3 칸 전진
        for k in range(1, 4):
            dy, dx, dd = yy + dty[d] * k, xx + dtx[d] * k, d
            # 배열을 벗어난 경우, 중간에 벽으로 막힌 경우 -> 다음을 진행할 수 없음.
            if dy < 0 or dx < 0 or dy > m - 1 or dx > n - 1: break
            if arr[dy][dx] == 1: break
            if used[dy][dx][dd] == 1: continue
            used[dy][dx][dd] = 1
            q.append([dy, dx, dd, cnt + 1])

        # 방향 전환
        for k in change_d[d]:
            if used[yy][xx][k] == 1: continue
            used[yy][xx][k] = 1
            q.append([yy, xx, k, cnt + 1])


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
sy, sx, sd = map(int, input().split())
ey, ex, ed = map(int, input().split())
print(bfs())