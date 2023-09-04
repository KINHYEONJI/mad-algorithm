from collections import deque
def bfs():
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            dx = directx[i] + x
            dy = directy[i] + y
            dz = directz[i] + z
            if dx<0 or dy<0 or dz<0 or dx>m-1 or dy>n-1 or dz>h-1:
                continue
            if tomato[dz][dy][dx] == 0:
                tomato[dz][dy][dx] = tomato[z][y][x]+1
                q.append([dz,dy,dx])


m,n,h = map(int,input().split())
tomato = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
directx = [0,0,-1,1,0,0]
directy = [1,-1,0,0,0,0]
directz = [0,0,0,0,1,-1]



q = deque()
for i in range(h):
    for k in range(n):
        for j in range(m):
            if tomato[i][k][j] == 1:
                q.append([i,k,j])
bfs()
Max = 0
for i in range(h):
    for k in range(n):
        for j in range(m):
            if Max<tomato[i][k][j]:
                Max = tomato[i][k][j]
flag = 0
for i in range(h):
    for k in range(n):
        for j in range(m):
            if tomato[i][k][j] == 0:
                flag=1



if flag == 1:
    print(-1)
elif Max == 1:
    print(0)
else:
    print(Max-1)