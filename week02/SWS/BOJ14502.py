from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
deq = deque()

directy = [0,0,1,-1, 0]
directx = [1,-1,0,0, 0]

def virus(i, j):
    for k in range(5):
        dy = i + directy[k]
        dx = j + directx[k]
        if dx < 0 or dy < 0 or dx > N-1 or dy > M-1:continue
        if arr[dy][dx] == 1: continue
        arr[dy][dx] = 2

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus(i, j)

print()
for i in arr:
    print(*i)