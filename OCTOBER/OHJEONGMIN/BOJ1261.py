#bfs 백트래킹
import sys
from collections import deque


def bfs():
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y + dry[i]
            dx = x + drx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>m-1:
                continue
            if dist[dy][dx]==-1:
                if lst[dy][dx]==0:
                    q.appendleft([dy,dx])
                    dist[dy][dx] = dist[y][x]
                elif lst[dy][dx]==1:
                    q.append([dy,dx])
                    dist[dy][dx]=dist[y][x]+1
       


m,n = map(int,input().split())
lst = [list(map(int,input())) for _ in range(n)]
cnt_lst = []
q = deque()
q.append([0,0])
visit = [[0]*m for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
dist[0][0]=0
dry = [1,-1,0,0]
drx = [0,0,-1,1]


bfs()

print(dist[n-1][m-1])