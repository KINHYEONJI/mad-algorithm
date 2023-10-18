from collections import deque

dir = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs():
    visited = [[21e8]*m for _ in range(n)]
    visited[0][0] = 0
    q = deque([[0,0,0]])
    while q:
        y,x,c = q.popleft()
        for i in range(4):
            dy = y + dir[i][0]
            dx = x + dir[i][1]
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if arr[dy][dx] == 0:
                if visited[dy][dx] > c:
                    visited[dy][dx] = c
                    q.append([dy,dx,c])
            else:
                if visited[dy][dx] > c + 1:
                    visited[dy][dx] = c + 1
                    q.append([dy,dx,c+1])

    return print(visited[n-1][m-1])

m,n = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
bfs()