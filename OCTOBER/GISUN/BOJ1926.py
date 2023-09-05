from collections import deque
n,m=map(int,input().split())
# used=[[0]*n for i in range(n)] 
arr=[]
cnt=0
max=0
dxl=[0,0,1,-1]
dyl=[1,-1,0,0]
for i in range(n):
    arr.append(list(map(int,input().split())))

def bfs(y,x):
    global max
    # used[y][x]=1
    cnt_1=1
    q=deque()
    q.append([y,x])
    arr[y][x]=0
    while q:
        y,x=q.popleft()
        for i in range(4):
            dy=y+dyl[i]
            dx=x+dxl[i]
            if dy>n-1 or dy<0 or dx<0 or dx>m-1:continue
            # if used[dy][dx]==1:continue
            if arr[dy][dx]==1:
                arr[dy][dx]=0
                cnt_1+=1
                q.append([dy,dx])
                
    if cnt_1>max:
        max=cnt_1
                    

for i in range(n):
    for j in range(m):
        if arr[i][j]==1: 
            cnt+=1
            bfs(i,j)

print(cnt)
print(max)