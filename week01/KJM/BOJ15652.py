n,m = map(int,input().split())

# branch = n
# level = m
path = [0] * m
visited = [False] * n

def abc(level):
    
    if level == m:
        for i in range(m):
            print(path[i],end=' ')
        print()
        return
    

    for i in range(n):
        if level == 0 or i+1 >= path[level-1]:
            path[level] = i + 1
            abc(level+1)

abc(0)