import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global cnt,keys
    visited = [[0]*w for _ in range(h)]
    diry = [-1,0,1,0]
    dirx = [0,1,0,-1]
    q = deque()
    flag = 0
    for i in ent:
        q.append(i)
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y + diry[i]
            dx = x + dirx[i]
            if dy < 0 or dx < 0 or dy > h-1 or dx > w-1: continue
            if visited[dy][dx] == 0 and arr[dy][dx] != '*':
                visited[dy][dx] = 1
                if arr[dy][dx] == '.':
                    q.append([dy,dx])

                elif arr[dy][dx] == '$':
                    q.append([dy,dx])
                    arr[dy][dx] = '.'
                    cnt += 1

                elif arr[dy][dx].islower():
                    q.append([dy,dx])
                    keys.append(arr[dy][dx])
                    arr[dy][dx] = '.'
                    flag = 1

    if flag:
        return 1
    else:
        return 0

def change():
    global keys
    for i in range(h):
        for j in range(w):
            if arr[i][j].isupper() and (arr[i][j].lower() in keys):
                arr[i][j] = '.'
                if i == 0 or j == 0 or i == h-1 or j == w-1:
                    ent.append([i,j])

for _ in range(int(input())):
    h,w = map(int,input().split())
    arr = [list(input().rstrip()) for _ in range(h)]
    keys = list(input().rstrip())

    ent = []
    cnt = 0
    for i in range(h):
        for j in range(w):
            if i == 0 or j == 0 or i == h-1 or j == w-1:
                if arr[i][j] == '.':
                    ent.append([i,j])
                elif arr[i][j] == '$':
                    cnt += 1
                    arr[i][j] = '.'
                    ent.append([i,j])
                elif arr[i][j].isupper() and (arr[i][j].lower() in keys):
                    arr[i][j] = '.'
                    ent.append([i,j])
                elif arr[i][j].islower():
                    ent.append([i,j])
                    keys.append(arr[i][j])
                    arr[i][j] = '.'

    if not ent:
        print(0)
    else:
        change()
        while bfs():
            change()
        print(cnt)