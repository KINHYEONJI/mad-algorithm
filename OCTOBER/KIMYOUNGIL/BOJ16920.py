from collections import deque
n,m,p = map(int,input().split())
si = [0] + list(map(int,input().split()))
arr = [list(input()) for _ in range(n)]

diry = [-1,0,1,0]
dirx = [0,1,0,-1]

def bfs():
    q = deque(deque() for _ in range(p+1))
    for i in lst:
        for j in i:
            q[j[2]].append(j)
    visited = [[0]*m for _ in range(n)]
    while q:
        l = []
        a_q = q.popleft()
        while a_q:
            y,x,a,b,c = a_q.popleft()
            if c == b:
                break
            for i in range(4):
                dy = y + diry[i]
                dx = x + dirx[i]
                if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
                if arr[dy][dx] == '.' and abs(y-dy)+abs(x-dx) <= b and visited[dy][dx] == 0:
                    visited[dy][dx] = 1
                    arr[dy][dx] = a
                    cnt[a] += 1
                    a_q.append([dy,dx,a,b,c+1])
                    l.append([dy,dx,a,b,0])
        if l:
            q.append(deque(l))

lst = [[] for _ in range(p+1)]
for i in range(n):
    for j in range(m):
        if arr[i][j].isdigit():
            lst[int(arr[i][j])].append([i,j,int(arr[i][j]),si[int(arr[i][j])],0])

cnt = [0]*(p+1)
for i in range(p+1):
    cnt[i] += len(lst[i])

bfs()
print(*cnt[1:])