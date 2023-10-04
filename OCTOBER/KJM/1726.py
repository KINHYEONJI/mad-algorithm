import sys
from collections import deque

n,m = map(int,input().split())
arr = ['/' * (m+1)] + [ ['/']+ list(map(int,input().split())) for _ in range(n)]
sy,sx,s_head = map(int,input().split())
ey,ex,e_head = map(int,input().split())

'''
동 서 남 북
1 2 3 4 
'''
diy = [0,0,0,1,-1]
dix = [0,1,-1,0,0]
rotate = {1:[3,4], 2:[3,4], 3:[1,2], 4:[1,2]}
def bfs(sy,sx,s_head,commands):
    visit = [[[False] * 5 for _ in range(m+1)] for _ in range(n+1)]
    q = deque()
    q.append([sy,sx,s_head,commands])
    visit[sy][sx][s_head] = True

    while q:
        ny,nx,n_head,commands = q.popleft()

        if ny == ey and nx == ex and n_head == e_head:
            return commands

        for go_X in (1,2,3):
            dy = ny + (diy[n_head] * go_X)
            dx = nx + (dix[n_head] * go_X)

            if dy<1 or dx<1 or dy>=n+1 or dx>=m+1 or arr[dy][dx] == 1: break

            if not visit[dy][dx][n_head]:
                visit[dy][dx][n_head] = True
                q.append([dy,dx,n_head,commands+1])

        #좌로 돌든 우로 돌든 순서 상관없음 어차피 다 돌아봐야하니까
        for next_head in rotate[n_head]:
            if not visit[ny][nx][next_head]:
                visit[ny][nx][next_head] = True
                q.append([ny,nx,next_head,commands+1])


res = bfs(sy,sx,s_head,0)
print(res)
