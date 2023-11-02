import sys
from collections import deque
input = sys.stdin.readline

def bfs(a,b):
    q = deque([[a,b]])
    while q:
        y,x = q.popleft()
        if abs(y-gy) + abs(x-gx) <= 1000:
            return print('happy')
        
        for i in range(n):
            if visited[i] == 0:
                if abs(y-arr[i][0]) + abs(x-arr[i][1]) <= 1000:
                    visited[i] = 1
                    q.append(arr[i])
    return print('sad')

for _ in range(int(input())):
    n = int(input())
    sy,sx = map(int,input().split())
    arr = deque(list(map(int,input().split())) for _ in range(n))
    gy,gx = map(int,input().split())

    visited = [0]*n
    bfs(sy,sx)