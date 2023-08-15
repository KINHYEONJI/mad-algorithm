n, m = map(int,input().split())

# level = m
# branch = n
node = list(map(int,input().split()))
node.sort()
path = [0] * m


def abc(level):
    
    if level == m:
        for i in range(m):
            print(path[i],end=' ')
        print()
        return
    
    for i in range(n):
        
        if level == 0 or node[i] > path[level-1]:
            path[level] = node[i]
            abc(level+1)
        


abc(0)