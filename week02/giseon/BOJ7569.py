from collections import deque
queue=deque()
width,length,high=map(int,input().split())
arr=[]
lst=[]
dzl=[0,0,0,0,1,-1]
dyl=[1,-1,0,0,0,0]
dxl=[0,0,1,-1,0,0]
for i in range(high):
    lst=[]
    for j in range(length):
        lst.append(list(map(int,input().split())))
    
        for k in range(width):
            if lst[j][k]==1:
                queue.append([i,j,k])
    arr.append(lst)

while queue:
    z,y,x=queue.popleft()
    for i in range(6):
        dz=z+dzl[i]
        dx=x+dxl[i]
        dy=y+dyl[i]
        if 0<=dz<high and 0<=dx<width and 0<=dy<length and arr[dz][dy][dx]==0:
            arr[dz][dy][dx]=arr[z][y][x]+1
            queue.append([dz,dy,dx])

# print(arr)

day = 0
for i in arr:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)
# print(*arr)

# import sys
# from collections import deque
# m,n,h = map(int,input().split()) # mn크기, h상자수
# graph = []
# queue = deque([])
 
# for i in range(h):
#     tmp = []
#     for j in range(n):
#         tmp.append(list(map(int,sys.stdin.readline().split())))
#         for k in range(m):
#             if tmp[j][k]==1:
#                 queue.append([i,j,k])
#     graph.append(tmp)
    
# dx = [-1,1,0,0,0,0]
# dy = [0,0,1,-1,0,0]
# dz = [0,0,0,0,1,-1]
# while(queue):
#     x,y,z = queue.popleft()
    
#     for i in range(6):
#         a = x+dx[i]
#         b = y+dy[i]
#         c = z+dz[i]
#         if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
#             queue.append([a,b,c])
#             graph[a][b][c] = graph[x][y][z]+1

# print(*graph)