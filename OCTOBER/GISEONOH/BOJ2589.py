import copy
from  collections import deque

m,n = map(int,(input().split())) #세로 가로

arr = [list(input()) for i in range(m)]
dxl=[0,0,1,-1]
dyl=[1,-1,0,0]

# print(arr)
def bfs(y,x):
    global arr
    arr_c=copy.deepcopy(arr)
    # print(arr_c)
    q= deque()
    q.append([y,x,0])
    arr_c[y][x]=0
    while q:
        y,x,c= q.popleft()
        for i in range(4):
            dy = y + dyl[i]
            dx = x + dxl[i]
            if -1<dy<m and -1<dx<n and arr_c[dy][dx] == 'L':
                    arr_c[dy][dx] = c
                    q.append([dy,dx,c+1])

    return c

# arr_c=copy.deepcopy(arr)
# print(arr_c)        
# print(1)


max =0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 'L':
            ct=bfs(i,j)
            if ct>max:
                max=ct

print(max)

