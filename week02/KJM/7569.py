from collections import deque
import sys
sys.stdin = open('input.txt','r')

M,N,H = map(int,input().split()) # 가로,세로,높이
arr = []
for k in range(H):
    layer = []
    for i in range(N):
        row = list(map(int,input().split()))
        layer.append(row)
    arr.append(layer)

def bfs():
    q = deque()

    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[k][i][j] == 1:
                    q.append([k,i,j,2])

    while q:
        z,y,x,days = q.popleft()

        diy = [-1,1,0,0,0,0]
        dix = [0,0,-1,1,0,0]
        diz = [0,0,0,0,-1,1]

        for i in range(6):
            dy = y+diy[i]
            dx = x+dix[i]
            dz = z+diz[i]

            if dy<0 or dx<0 or dz<0: continue
            if dy>=N or dx>=M or dz>=H: continue

            if arr[dz][dy][dx] == 0:
                arr[dz][dy][dx] = days
                q.append([dz,dy,dx,days+1])

bfs()
# 체크
max_day = -21e8
for k in range(H):
    for i in range(N):
        for j in range(M):
            max_day = max(max_day,arr[k][i][j])

#
# for ar in arr:
#     for a in ar:
#         print(*a)

flag =0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 0:
                flag = 1
                break

if flag:
    print(-1)

elif max_day == 1:
    print(0)
else:
    print(max_day-1)
