N,M = map(int,input().split())
def abc(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        path[level] = i+1
        abc(level+1)
path = ['']*M
abc(0)