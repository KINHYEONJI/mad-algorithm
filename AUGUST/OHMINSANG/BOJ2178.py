"""
bfs 탐색
"""
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
q.append((0, 0))
while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if arr[ny][nx] == 1:
                arr[ny][nx] = arr[y][x] + 1
                if ny == N - 1 and nx == M - 1:
                    print(arr[ny][nx])
                    q.clear()
                q.append((ny, nx))
