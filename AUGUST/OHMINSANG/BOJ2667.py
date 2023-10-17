"""
23 / 08 / 16 알고 스터디
단지번호붙이기
"""
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
used = [[-1] * n for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
cnt = 0
lst = []


for x in range(n):
    for y in range(n):
        if arr[x][y] == 1:
            q = deque()
            q.append([x, y])
            used[x][y] = 1
            size = 0
            while q:
                yy, xx = q.popleft()
                size += 1
                arr[yy][xx] = 0
                for i in range(4):
                    ny = yy + dy[i]
                    nx = xx + dx[i]
                    if (0 <= ny < n and 0 <= nx < n and
                        arr[ny][nx] == 1 and used[ny][nx] == -1):
                        used[ny][nx] =1
                        q.append([ny, nx])
            cnt += 1
            lst.append(size)

print(cnt)
lst.sort()
for ans in lst:
    print(ans)