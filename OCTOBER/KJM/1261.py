import sys
sys.stdin = open('input.txt','r')
#

from collections import deque

m,n = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n) ]

visit = [[-1] * (m) for _ in range(n)]

def bfs(sy,sx):
    q = deque()
    q.append([sy,sx])
    visit[sy][sx] = 0

    while q:
        y,x = q.popleft()
        diy = [-1,1,0,0]
        dix = [0,0,-1,1]

        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]
            if dy<0 or dx<0 or dy>=n or dx>=m: continue
            if visit[dy][dx] != -1:
                continue

            # 벽이면 오른쪽 큐 삽입
            if arr[dy][dx] == 1:
                q.append([dy,dx])
                visit[dy][dx] = visit[y][x] + 1
            else:
                # 길이면 q의 왼쪽에
                # 더 빨리 탐색하기 위해
                q.appendleft([dy,dx])
                visit[dy][dx] = visit[y][x]


bfs(0,0)
print(visit[n-1][m-1])