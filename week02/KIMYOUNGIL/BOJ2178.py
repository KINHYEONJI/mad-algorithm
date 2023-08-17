from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dist = [[0]*m for _ in range(n)]

diry = [-1,0,1,0]
dirx = [0,1,0,-1]
def bfs(a,b):
    q = deque()
    q.append([a,b])
    dist[a][b] = 1
    while q:
        y,x = q.popleft()
        if y == n-1 and x == m-1:
            print(dist[y][x])
            break
        for i in range(4):
            dy = y + diry[i]
            dx = x + dirx[i]
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if not dist[dy][dx] and arr[dy][dx] == 1:
                dist[dy][dx] = dist[y][x] +1
                q.append([dy,dx])

bfs(0,0)