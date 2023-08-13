n,m = map(int,input().split())
path = [0]*m

def product(lev):
    if lev == m:
        for i in range(m):
            print(path[i],end=' ')
        print()
        return

    for i in range(n):
        path[lev] = i+1
        product(lev+1)

product(0)