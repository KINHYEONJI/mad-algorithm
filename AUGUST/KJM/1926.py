from collections import deque

import sys
sys.stdin = open('input.txt','r')
n,m = map(int,input().split())

arr = [ list(map(int,input().split())) for _ in range(n) ]

def bfs(i,j):
    q = deque()
    q.append([i,j])
    arr[i][j] = 0
    size = 0

    while q:
        y,x = q.popleft()
        size += 1
        # print(y,x,size)

        diy = [-1,1,0,0]
        dix = [0,0,-1,1]
        for i in range(4):
            dy = y + diy[i]
            dx = x + dix[i]
            if dy<0 or dx<0 or dy>=n or dx>=m: continue
            if arr[dy][dx] != 1: continue
            arr[dy][dx] = 0
            q.append([dy,dx])

    return size

max_v = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            max_v = max(max_v,bfs(i,j))
            cnt += 1

print(cnt)
print(max_v)