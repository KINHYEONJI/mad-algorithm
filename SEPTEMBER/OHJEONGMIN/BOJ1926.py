from collections import deque
def bfs():
    global cnt,area_cnt

    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>m-1 or paper[dy][dx]==0:
                continue
            paper[dy][dx]=0
            q.append([dy,dx])
            area_cnt+=1

n,m = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(n)]
q = deque()
area = []
cnt,flag = 0,0
directy = [1,-1,0,0]
directx = [0,0,-1,1]
for i in range(n):
    for k in range(m):
        if paper[i][k]==1:
            paper[i][k]=0
            area_cnt=1
            q.append([i,k])
            bfs()
            area.append(area_cnt)
            cnt+=1

if area:
    print(cnt)
    print(max(area))
else:
    print(len(area))
    print(0)