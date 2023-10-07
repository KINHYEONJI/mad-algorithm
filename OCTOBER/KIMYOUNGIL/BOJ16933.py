from collections import deque

dir = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs():
    visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
    visited[0][0] = [1]*(k+1)
    q = deque([[0,0,1,0,1]])
    while q:
        y,x,a,b,c = q.popleft()
        if y == n-1 and x == m-1:
            return print(c)
        for i in range(4):
            dy = y + dir[i][0]
            dx = x + dir[i][1]
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if visited[dy][dx][b] == 0:
                if arr[dy][dx] == 0:
                    visited[dy][dx][b] = c+1
                    q.append([dy,dx,a+1,b,c+1])
                else:
                    if b < k and visited[dy][dx][b+1] == 0:
                        if a%2:
                            visited[dy][dx][b+1] = c+1
                            q.append([dy,dx,a+1,b+1,c+1])
                        else: q.append([y,x,a+1,b,c+1])
    return print(-1)

n,m,k = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
bfs()