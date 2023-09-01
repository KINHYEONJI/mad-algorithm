from collections import deque
import copy
n,m=map(int,input().split())                     #세로 가로
arr=[]
q=deque()
lst_0=[]                                         #0의 좌표를 받을 리스트
lst_2=[]                                         #2의 좌표를 받을 리스트
dxl=[0,0,1,-1]
dyl=[1,-1,0,0]
max=0
for i in range(n):                               #리스트 선언
    arr.append(list(map(int,input().split())))
# print(arr)
def bfs():                   #bfs 함수 선언 바이러스 퍼트리는 용
    global q,arr
    q_1=copy.deepcopy(q)     #다수의 bfs 사용 위해 백업본 계속 복사해서 사용
    # print(q_1)
    while q_1:
        y,x=q_1.popleft()
        for i in range(4):
            dx=x+dxl[i]
            dy=y+dyl[i]
            if -1<dy<n and -1<dx<m:
                if arr[dy][dx]==2:continue
                if arr[dy][dx]==1:continue

                arr[dy][dx]=2
                q_1.append([dy,dx])

def dfs(now,level):                  #(0인 빈칸 중) 3개의 벽을 고르기 위한 dfs(조합) 
    global max,arr
    cnt=0
    if level==3:
        backup=copy.deepcopy(arr)    #arr을 백업해둔다 원본 데이터를 쓰고 복구하기위해서
        bfs()
        for i in range(n):           #좌표를 리스트에 어펜드
            for j in range(m):
                if arr[i][j]==0:
                    cnt+=1
        if max<cnt:
            max=cnt
        arr=backup                   #arr 복구
        # print(cnt)
        return
    
    for i in range(now,len(lst_0)):
        y,x=lst_0[i]
        if arr[y][x]==1:continue
        arr[y][x]=1
        dfs(i+1,level+1)
        arr[y][x]=0




for i in range(n):           #좌표를 리스트에 어펜드
    for j in range(m):
        if arr[i][j]==0:
            lst_0.append([i,j])       #dfs 용 미리 받아두기
        if arr[i][j]==2:
            q.append([i,j])           #bfs 용 미리 받아두기

dfs(0,0)
print(max)