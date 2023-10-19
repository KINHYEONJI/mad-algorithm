from collections import deque
import sys
input = sys.stdin.readline


dxl = [ 0,0,1,-1]
dyl = [ 1,-1,0,0]


t = int(input())

def bfs(y,x):
    q=deque()
    q.append([y,x])
    lst[y][x] = 0
    while q:
        y,x = q.popleft()
        # print(y,x)
        for i in range(4):
            dy = y + dyl[i]
            dx = x + dxl[i]
            if -1<dy<w and -1<dx<l:
                if lst[dy][dx] == 1:
                    lst[dy][dx] = 0
                    q.append([dy,dx])




for tc in range(t):
    l, w, c = map(int,input().split())
    lst= [ [0]* l for i in range(w)]
    # print(lst)
    for i in range(c):
        x,y = map(int,input().split())
        lst[y][x] = 1
    cnt=0
    for i in range(w):
        for j in range(l):
            if lst[i][j] == 0:continue
            cnt+=1
            # print(lst)
            bfs(i,j)

    print(cnt)