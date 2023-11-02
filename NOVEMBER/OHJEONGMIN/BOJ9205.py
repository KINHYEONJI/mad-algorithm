from collections import deque
#bfs
def bfs():
    while q:
        x,y = q.popleft()
        if abs(x-lst[-1][0])+abs(y-lst[-1][1])<=1000:
            return print('happy')
        for i in range(n):
            if visit[i]==-1:
                a,b = mart[i]
                if abs(x-a)+abs(y-b)<=1000:
                    visit[i] = 1
                    q.append([a,b])
    return print('sad')

t = int(input())
for test_case in range(t):
    #편의점의 개수
    n = int(input())
    lst = []
    mart = []
    for i in range(n+2):
        a, b = list(map(int, input().split()))
        if i==0 or i==n+1:
            lst.append([a,b])
        else:
            mart.append([a,b])
    visit = [-1]*(n+1)
    q = deque()
    q.append([lst[0][0],lst[0][1]])
    bfs()
