#0인 좌표의 모든 조합을 구해서 바이러스가 최소한으로 퍼질 수 있게 코드 짬

from collections import deque
import copy
def dfs(level,start):
    global Max,result_lst
    if level == 3:
        cnt,Sum=0,0
        for i in range(3):
            result_lst[path[i][0]][path[i][1]]=1  # bfs로 순회하기 전 벽세우기
        bfs()
        for i in range(n):
            Sum+=result_lst[i].count(0)
        if Sum>Max:
            Max = Sum
        result_lst = copy.deepcopy(lst)  #모든 배열을 순회한뒤 처음 배열로 초기화
        return
    for i in range(start,len(arr)):  # 0의 좌표의 가능한 모든 조합 찾기
        path.append(arr[i])
        dfs(level+1,i+1)

        path.pop()

def bfs():
    global result_lst,q
    qq = copy.deepcopy(q)  #q를 deepcopy하여 bfs 돌때마다 초기화

    while qq:
        y,x = qq.popleft()
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy<0 or dx<0 or dx>m-1 or dy>n-1:
                continue

            if result_lst[dy][dx] ==0:
                result_lst[dy][dx] = 2
                qq.append([dy,dx])


n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
result_lst = copy.deepcopy(lst)
directy = [1,-1,0,0]
directx = [0,0,-1,1]
q = deque()
arr = []
for i in range(n):
    for k in range(m):
        if lst[i][k]==2:
            q.append([i,k])     #바이러스의 좌표 찾기
        elif lst[i][k]==0:
            arr.append([i,k])   #0의 모든 좌표 찾기
Max = 0
path = []
dfs(0,0)

print(Max)