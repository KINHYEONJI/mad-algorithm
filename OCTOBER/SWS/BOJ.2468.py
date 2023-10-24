# import sys
# sys.stdin = open('input.txt','r')
from collections import deque

N = int(input())
lst = []
ret = 0

for i in range(N):
    lst.append(list(map(int, input().split())))
    for j in range(N):
        if lst[i][j] > ret:
            ret = lst[i][j]

directy = [0,0,1,-1]
directx = [1,-1,0,0]
def bfs(i,j, num,  visited):
    deq = deque()
    deq.append((i,j))
    visited[i][j] = 1

    while deq:
        now = deq.popleft()
        nowy, nowx = now
        for q in range(4):
            dy = nowy + directy[q]
            dx = nowx + directx[q]
            if dy < 0 or dy > N-1 or dx < 0 or dx > N-1 : continue
            if visited[dy][dx] == 1: continue
            if lst[dy][dx] > num:
                visited[dy][dx] = 1
                deq.append((dy,dx))


result = 0
for i in range(ret):
    visited = [[0] * N for i in range(N)]
    cnt = 0

    for j in range(N):
        for k in range(N):
            if lst[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)