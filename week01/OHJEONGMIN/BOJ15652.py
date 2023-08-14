N,M = map(int,input().split())
def abc(level,start):
    if level==M:
        print(*path)
        return
    for i in range(start,N):
        path[level] = i+1
        abc(level+1,i)

path = ['']*M
abc(0,0)