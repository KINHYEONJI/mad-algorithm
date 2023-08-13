# 순열
N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
def abc(level):
    if level == M:
        print(*path)
        return
    for i in range(N):
        if visited[i]==1:
            continue
        visited[i]=1
        path[level] = num[i]
        abc(level+1)
        visited[i]=0
path = ['']*M
visited = [0]*(N+1)
abc(0)