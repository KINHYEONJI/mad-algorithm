#조합
N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
def abc(level,start):
    if level==M:
        print(*path)
        return

    for i in range(start,N):
        path[level] = lst[i]
        abc(level+1,i+1)


path = ['']*M
abc(0,0)