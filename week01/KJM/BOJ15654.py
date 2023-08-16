n,m = map(int,input().split())

# level = m
# branch = n
node = list(map(int,input().split()))
node.sort()
path = [0] * m 
visited = [False]*n

def abc(level):
    
    if level == m:
        for i in range(level):
            print(path[i],end=' ')
        print()
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            path[level] = node[i]
            abc(level+1)
            visited[i] = False
            

abc(0)