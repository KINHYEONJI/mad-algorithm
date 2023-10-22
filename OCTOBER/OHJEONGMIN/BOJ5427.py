import sys
from collections import deque
def fire_bfs():
    while q:
        y,x,cnt = q.popleft()
        for i in range(4):
            dy = y + dry[i]
            dx = x + drx[i]
            if dy<0 or dy>h-1  or dx<0 or dx>w-1:
                continue
            if lst[dy][dx]=='#':
                continue
            if visit[dy][dx]==1:
                continue
            visit[dy][dx]=1
            result[dy][dx] = cnt+1
            q.append([dy,dx,cnt+1])
def s_bfs():
    while s_q:

        y,x,cnt = s_q.popleft()
        for i in range(4):
            dy = y + dry[i]
            dx = x + drx[i]
            if dy<0 or dy>h-1 or dx<0 or dx>w-1:
                return cnt+1
            if lst[dy][dx]=='#':
                continue
            if s_visit[dy][dx]==-1:
                s_visit[dy][dx]=1
                if result[dy][dx]==-1:
                    s_q.append([dy,dx,cnt+1])
                elif result[dy][dx]>cnt+1:
                    s_q.append([dy,dx,cnt+1])



tc = int(input())
for test_case in range(tc):
    w,h = map(int,input().split())
    visit = [[-1]*w for _ in range(h)]
    result = [[-1]*w for _ in range(h)]
    s_visit = [[-1]*w for _ in range(h)]
    lst = [list(input()) for _ in range(h)]
    q = deque()
    s_q = deque()
    for i in range(h):
        for k in range(w):
            if lst[i][k]=='@':
                s_q.append([i,k,0])
            if lst[i][k]=='*':
                visit[i][k]=1
                q.append([i,k,0])
                result[i][k]=0
    dry = [-1,1,0,0]
    drx = [0,0,-1,1]
    fire_bfs()
    ret = s_bfs()
    if ret:
        print(ret)
    else:
        print('IMPOSSIBLE')