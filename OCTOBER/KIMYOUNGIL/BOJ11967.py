from collections import deque

n,m = map(int,input().split())
lst = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,a,b = map(int,input().split())
    lst[x-1][y-1].append([a-1,b-1])

dir = [[0,1],[0,-1],[-1,0],[1,0]]

def bfs():
    q = deque([[0,0]])
    cnt = 1
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = 1
    light = [[0]*n for _ in range(n)]
    light[0][0] = 1
    while q:
        y,x = q.popleft()
        for i,j in lst[y][x]:
            if light[i][j] == 0:
                light[i][j] = 1
                cnt += 1
                for k in range(4):
                    dy = i + dir[k][0]
                    dx = j + dir[k][1]
                    if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:continue
                    if visited[dy][dx]:
                        q.append([dy,dx])

        for k in range(4):
            dy = y + dir[k][0]
            dx = x + dir[k][1]
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:continue
            if light[dy][dx] == 1 and visited[dy][dx] == 0:
                visited[dy][dx] = 1
                q.append([dy,dx])

    return print(cnt)
bfs()