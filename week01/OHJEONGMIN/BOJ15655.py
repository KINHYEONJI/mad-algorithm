#조합
N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
def abc(level,start):
    if level==M:
        print(*Path)
        return

    for i in range(start,N):
        Path[level] = lst[i]
        abc(level+1,i+1)


Path = ['']*M
abc(0,0)