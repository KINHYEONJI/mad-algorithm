n,m = map(int,input().split())
ry,rx,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
dir = [[-1,0],[0,1],[1,0],[0,-1]]
while 1:
    if arr[ry][rx] == 0:
        cnt += 1
        arr[ry][rx] = 2
        
    flag = 0
    for i in range(4):
        dy = ry + dir[i][0]
        dx = rx + dir[i][1]
        if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
        if arr[dy][dx] == 0: flag = 1

    if flag == 1:
        d -= 1
        dy = ry + dir[d%4][0]
        dx = rx + dir[d%4][1]
        if 0 <= dy < n and 0 <= dx < m:
            if arr[dy][dx] == 0: ry = dy; rx = dx

    elif flag == 0:
        dy = ry + dir[(d-2)%4][0]
        dx = rx + dir[(d-2)%4][1]
        if 0 <= dy < n and 0 <= dx < m:
            if arr[dy][dx] != 1: ry = dy; rx = dx
            else: break  
        else: break

print(cnt)