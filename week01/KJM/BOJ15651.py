n,m = map(int,input().split())

# level = m
# branch = n
path = [0] * n


def abc(level):
    
    if level == m:
        for i in range(level):
            print(path[i],end=' ')
        print()
        return
    
    for i in range(n):
        path[level] = i+1
        abc(level+1)
    

abc(0)