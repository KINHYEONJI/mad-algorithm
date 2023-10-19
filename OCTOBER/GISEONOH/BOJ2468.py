n = int(input())
import copy
import sys
from collections import deque
input = sys.stdin.readline
lst=[list(map(int,input().split())) for _ in range(n)]
dxl = [1,-1,0,0]
dyl = [0,0,1,-1]
# lst_y=[]                                                      #없어도 밖에 선언 괜찮음

def count(x):
    global lst_y
    lst_y = copy.deepcopy(lst)
    # print(lst_y)
    cnt=0
    for i in range(n):
        for j in range(n):
            if lst_y[i][j] <= x:continue
            cnt += 1
            bfs(i,j,x)
    return cnt

def bfs(a,b,c):                                                 #함수 끼리 변수 넘길 때 인자로 넘기면되겠구나
    global lst_y                                                #새로만든 도화지 리스트 넘길 때 글로벌로 넘기기
    q = deque()
    lst_y[a][b] = c
    q.append([a,b])

    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y + dyl[i]
            dx = x + dxl[i]
            if -1 < dy < n and -1 < dx < n:
                if lst_y[dy][dx] > c:
                    lst_y[dy][dx] = c
                    q.append([dy,dx])

rs=1
#1인채로 시작 비가 안 올경우 안전지대는 1
for i in range(1,101):                       # 2>>1로 수정 비가 안 올경우(0) 부터 시작해주어야함 반례로 땅이 0인 경우의 조건이 있음
    a=count(i)
    if a>rs:
        rs=a

print(rs)