import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

row, col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]
used = [[0] * col for _ in range(row)]
cnt = 0
Max = 0
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
q = deque()

for y in range(row):
    for x in range(col):
        Sum = 1
        if arr[y][x] == 1 and used[y][x] == 0:
            used[y][x] = 1
            q.append([y, x])
            cnt += 1
            while q:
                yy, xx = q.popleft()
                for i in range(4):
                    ny, nx = yy + dy[i], xx + dx[i]
                    if 0 <= ny < row and 0 <= nx < col:
                        if arr[ny][nx] == 1 and used[ny][nx] == 0:
                            used[ny][nx] = 1
                            Sum += 1
                            q.append([ny, nx])
            Max = max(Max, Sum)
print(cnt)
print(Max)
