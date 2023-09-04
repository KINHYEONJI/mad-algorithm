#중복순열
N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

def abc(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        path[level] = lst[i]
        abc(level+1)

path = ['']*M
abc(0)