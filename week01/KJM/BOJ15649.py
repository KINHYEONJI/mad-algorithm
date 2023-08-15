n,m = map(int,input().split())

path = [0] * m # 조합 경우의 수
visited = [False] * n # 브랜치 만큼 배열

def abc(level):
    
    # 리프노드에 도달하면 모아뒀던 path 출력
    if level == m:
        for i in range(m):
            print(path[i],end=' ') 
        print()
        
        return
        
    
    # 한번 탐색했던 경로는 기억해두고 다음 레벨에서는 탐색하지 않도록
    # ex) 부모노드에서 1 탐색했다면 그 자식 노드들(브랜치) 중에서는 1을 선택안함
    for i in range(n):
        if not visited[i]:
            visited[i] = True 
            path[level] = i + 1
            abc(level+1)
            visited[i] = False
            
abc(0)
