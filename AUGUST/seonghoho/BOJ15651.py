#가장 기본적인 중복순열

n, m = map(int, input().split())
path = ['']*m

def abc(level):
    if level == m:
        for i in range(m):
            print(path[i], end=' ')
        print()
        return
    for i in range(1,n+1):
        path[level] = i
        abc(level+1)
abc(0)