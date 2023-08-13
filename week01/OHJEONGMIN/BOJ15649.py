N,M = map(int,input().split())
def abc(level):
    if level == M :
        print(*path)
        return
    for i in range(1,N+1):
        if visited[i]==1:
            continue
        path.append(i)
        visited[i] = 1
        abc(level+1)
        visited[i]=0
        path.pop()
visited = [0]*(N+1)
path = []
abc(0)