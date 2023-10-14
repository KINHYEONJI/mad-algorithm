from collections import deque
from itertools import combinations

dir = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(lst):
    visited = [[0]*m for _ in range(n)]
    time = [[0]*m for _ in range(n)]
    q = deque()
    for k in lst[0]:
        q.append(k+[0,1])
        visited[k[0]][k[1]] = 1
    for k in lst[1]:
        q.append(k+[0,-1])
        visited[k[0]][k[1]] = -1
    cnt = 0
    while q:
        y,x,c,p = q.popleft()
        if visited[y][x] == 2: continue
        for i in range(4):
            dy = y + dir[i][0]
            dx = x + dir[i][1]
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if (arr[dy][dx] == 1 or arr[dy][dx] == 2) and visited[dy][dx] == 0:
                visited[dy][dx] = p
                time[dy][dx] = c+1
                q.append([dy,dx,c+1,p])
            elif visited[dy][dx] == -p and time[dy][dx] == c+1:
                cnt += 1
                visited[dy][dx] = 2
    return cnt

n,m,g,r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

bae = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bae.append([i,j])

ans = 0
for i in combinations(bae,g+r):
    for j in combinations(i,g):
        lst = [list(j)]
        used = [0]*(g+r)
        for k in j:
            used[i.index(k)] = 1

        l = []
        for k in range(g+r):
            if used[k] == 0:
                l.append(i[k])
        lst.append(l)
        ret = bfs(lst)
        if ret > ans:
            ans = ret
print(ans)