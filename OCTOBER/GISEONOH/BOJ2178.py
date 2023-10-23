import sys
from collections import deque
input=sys.stdin.readline

n,m =map(int,input().split())

dxl=[1,-1,0,0]
dyl=[0,0,-1,1]

def dfs(x,y):
    q=deque()
    q.append([x,y,2])
    arr[0][0]=0

    while q:
        x,y,c =q.popleft()
        for i in range(4):
            dx=x+dxl[i]
            dy=y+dyl[i]
            if -1<dy<n and -1<dx<m:
                if arr[dy][dx]==1:
                    arr[dy][dx]=c
                    q.append([dx,dy,c+1])




#sys 사용해서 문자열 받을 때 끝에 /n 받아서 배열 오류 줄 맨끝에 공백 지워주는 메서드인 strip 사용
arr=[list(map(int,input().strip())) for i in range(n)]

# print(arr)

dfs(0,0)
# print(arr)
print(arr[n-1][m-1])