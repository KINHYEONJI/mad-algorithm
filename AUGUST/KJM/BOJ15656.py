n,m = map(int,input().split())

# level = m
# branch = n

node = list(map(int,input().split()))
node.sort()

path = [0]*m
visited = [False]*n


def abc(level):
    
    if level == m:
        for i in range(m):
            print(path[i],end=' ')
        print()
        return
    
    for i in range(n):
            path[level] = node[i]
            abc(level+1)


abc(0)