# import sys
# sys.stdin = open('input.txt')
from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(M)]
# 가중치 배열
visited = [[-1] * N for _ in range(M)]   

directy = [0,0,1,-1]
directx = [1,-1,0,0]

def bfs(y, x):
    deq = deque()
    deq.append((y,x))

    while deq:
        now = deq.popleft()
        now_y, now_x = now
        for i in range(4):
            dy = now_y + directy[i]
            dx = now_x + directx[i]
            if dy < 0 or dy > M-1 or dx < 0 or dx > N-1: continue
            if visited[dy][dx] == -1:
                if lst[dy][dx] == 0:
                    visited[dy][dx] = visited[now_y][now_x]
                    deq.appendleft((dy,dx))
                else:
                    visited[dy][dx] = visited[now_y][now_x] + 1
                    deq.append((dy,dx))
           


visited[0][0] = 0
bfs(0,0)

print(visited[M-1][N-1])