from collections import deque

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
directy = [0,0,1,-1]
directx = [1,-1,0,0]
def bfs(i, j):
    global q, Max
    q.append([i, j])
    count = 1
    while q:
        y,x = q.popleft()
        for k in range(4):
            dy = y + directy[k]
            dx = x + directx[k]
            if dx < 0 or dy < 0 or dx > M-1 or dy > N-1:continue
            if arr[dy][dx] == 1 and used[dy][dx] == 0:
                used[dy][dx] = 1
                count += 1
                q.append([dy,dx])
    if count > Max:
        Max = count

used = [[0]*M for _ in range(N)]
Max = 0  
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and used[i][j] == 0:
            used[i][j] = 1
            cnt += 1
            bfs(i, j)
print(cnt)
print(Max)