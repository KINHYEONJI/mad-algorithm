from collections import deque
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

diry = [-1,0,1,0]
dirx = [0,1,0,-1]

def bfs(a,b):
    global Max
    q = deque([[a,b]])
    wid = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y + diry[i]
            dx = x + dirx[i]
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if arr[dy][dx] == 1 and visited[dy][dx] == 0:
                visited[dy][dx] = 1
                wid += 1
                q.append([dy,dx])

    if wid > Max:
        Max = wid

Max = 0
cnt = 0
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            cnt += 1
            bfs(i,j)

print(cnt)
print(Max)