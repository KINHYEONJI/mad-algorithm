n,m = map(int,input().split())


# brach = n
# level = m

path = [0] * m
visited = [False] * n 

def abc(level):
    
    if level == m:
        for i in range(level):
            print(path[i],end=' ')
        print()
        
        return
    
    for i in range(n):
        # 앞으로 탐색할 자식노드는 부모노드보다 커야함
        if  level == 0 or path[level-1] < i+1:
            path[level] = i+1
            abc(level+1)

abc(0)