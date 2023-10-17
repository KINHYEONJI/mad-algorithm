import sys
sys.stdin = open('input.txt','r')

'''
방향전환할 때 갯수를 따로 기록하고
최소인경우로만 
'''
from collections import deque

m,n = map(int,input().split())
arr = [list(input()) for _ in range(n)]
inf = int(21e8)
rotates = [[inf]*m for _ in range(n)]
mirrors = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'C':
            mirrors.append([i,j])

y1,x1 = mirrors[0]
y2,x2 = mirrors[1]
arr[y2][x2] = '.'
diy = [-1,1,0,0]
dix = [0,0,-1,1]

def bfs(sy,sx):
    q = deque()
    q.append([sy,sx,0])
    rotates[sy][sx] = 0

    while q:
        y,x,cnt = q.popleft()

        for i in range(4):
            for k in range(1,max(n,m)+1):
                dy = y + (diy[i] * k)
                dx = x + (dix[i] * k)
                if dy<0 or dx<0 or dy>=n or dx>=m: continue
                if arr[dy][dx] == '*': break
                if arr[dy][dx] == '.':
                    if cnt < rotates[dy][dx]:
                        rotates[dy][dx] = cnt
                        q.append([dy,dx,cnt+1])

bfs(y1,x1)
print(rotates[y2][x2])
