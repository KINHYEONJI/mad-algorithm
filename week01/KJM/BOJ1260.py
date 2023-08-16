from collections import deque

n,m,v = map(int,input().split()) # vertex 수, edge 수, 시작번호


# 1. 비선형 구조인 그래프를 탐색을 위해 선형구조인 인접리스트로 변환
adj_list = [ [] for _ in range(n+1) ] # vertex만큼 인접리스트 만들어놓고

for _ in range(m): # edge 만큼 반복하면서 연결정보 추가 
    s,e = map(int,input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

# 문제가 오름차순으로 탐색하길 원하므로 인접리스트 오름차순 정렬
for i in range(1, n+1): # 0 행은 버리는 행이므로
    adj_list[i].sort()

# 2. v부터 DFS탐색 
visited = [False] * (n+1) # 방문 처리를 위한 vertex 수 만큼 배열 생성, 인덱스 편의를 위해 0번 인덱스를 버렸으므로 1추가

def dfs(now):
    visited[now] = True # 노드 방문처리 
    print(now,end=' ')
    
    for i in adj_list[now]:
        if not visited[i]: # 방문한 적 없으면 탐색
            dfs(i)

dfs(v)


# 3. v부터 BFS탐색
# 현재 기준 탐색할 수 있는 모든 인접노드를 큐에 저장
print()
visited2 = [False] * (n+1) # BFS용 방문처리배열

def bfs(now):
    
    q = deque() # Q를 데큐로 선언
    q.append(now) # 탐색 시작노드를 큐에 추가
    visited2[now] = True
    
    while q: # q가 빌 때 까지 반복 
        
        v = q.popleft() # 가장 처음 넣은 노드를 뽑고 v에 저장
        print(v,end=' ') # 탐색했던 노드라는 뜻이므로 출력 
        
        
        for i in adj_list[v]:
            if not visited2[i]:
                q.append(i)
                visited2[i] = True
        

bfs(v)
