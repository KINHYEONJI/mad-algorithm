import copy
from collections import deque


directy = [0,0,1,-1]
directx = [1,-1,0,0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
ans = 0

def abc():
    global ans
    w = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if w[i][j]==2:
                q.append([i,j])

    while q:
        x, y = q.popleft()
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if 0 <= dx < N and 0 <= dy < M:
                if w[dx][dy]==0:
                    w[dx][dy] = 2
                    q.append([dx,dy])
    cnt = 0
    for i in w:
        cnt+=i.count(0)
    ans = max(ans,cnt)


def wall(x):
    if x == 3:
        abc()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(x + 1)
                arr[i][j] = 0
wall(0)
print(ans)