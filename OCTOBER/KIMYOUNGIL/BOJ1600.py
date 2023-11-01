from collections import deque

dir = [[1,0],[-1,0],[0,1],[0,-1],
       [-1,-2],[-2,-1],[-2,1],[-1,2],
       [1,-2],[1,2],[2,-1],[2,1]]

def bfs():
    q = deque([[0,0,0,0]])
    visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
    while q:
        y,x,c,d = q.popleft()
        if y == n-1 and x == m-1:
            return print(c)

        for i in range(12):
            dy = y + dir[i][0]
            dx = x + dir[i][1]
            if d >= k and i > 3: continue
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if arr[dy][dx] == 0:
                if i > 3:
                    if d < k and visited[dy][dx][d+1] == 0:
                        visited[dy][dx][d+1] = c+1
                        q.append([dy,dx,c+1,d+1])
                else:
                    if visited[dy][dx][d] == 0:
                        visited[dy][dx][d] = c+1
                        q.append([dy,dx,c+1,d])
    return print(-1)

k = int(input())
m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
bfs()