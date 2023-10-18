#bfs
from collections import deque
import copy
def bfs():
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y + dry[i]
            dx = x + drx[i]
            if dy<0 or dx<0 or dx>n-1 or dy>n-1:
                continue
            if visit[dy][dx]==0:
                visit[dy][dx] = 1
                q.append([dy,dx])
                if new_lst[dy][dx]-num<=0:
                    new_lst[dy][dx]=0


def check():
    while c:
        y,x = c.popleft()
        for i in range(4):
            dy = y + dry[i]
            dx = x + drx[i]
            if dy < 0 or dx < 0 or dx > n - 1 or dy > n - 1:
                continue
            if c_visit[dy][dx]==0 and new_lst[dy][dx]!=0:
                c.append([dy,dx])
                new_lst[dy][dx]=0
                c_visit[dy][dx] = 1
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dry = [1,-1,0,0]
drx = [0,0,-1,1]
Max = 0
for i in range(n):
    for k in range(n):
        if lst[i][k]>Max:
            Max = lst[i][k]
num = 0
cnt_lst = []
while 1:
    if num>Max:
        break
    q = deque()
    new_lst = copy.deepcopy(lst)
    visit = [[0]*n for _ in range(n)]
    c_visit = [[0] * n for _ in range(n)]
    # 지도에서 높이가 0이 아닌곳을 q에 넣고 bfs돌리기
    for i in range(n):
        flag = 0
        for k in range(n):
            if new_lst[i][k] !=0:
                flag=1
                q.append([i,k])
                break
        if flag:
            break
    bfs()
    c = deque()
    cnt = 0
    # for i in new_lst:
    #     print(*i)
    # print()

    for i in range(n):
        flag=0
        for k in range(n):
            if new_lst[i][k]!=0:
                c.append([i,k])
                check()
                cnt+=1
    cnt_lst.append(cnt)
    num+=1
if max(cnt_lst)==0:
    print(1)
else:
    print(max(cnt_lst))

