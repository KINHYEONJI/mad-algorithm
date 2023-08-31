import sys
sys.stdin = open('week02/KJM/input.txt','r')

'''
최소신장트리 문제
집은 정점, 길은 간선이다

1) 간선의 정보를 모두 저장한다
2) 비용 기준으로 오름차순으로 간선을 정렬한다
3) 비용이 적은 간선부터 신장트리에 들어갈 정점으로 선택한다
4) 단, 그 과정에서 싸이클이 발생할 경우 선택하지 않는다
-> 싸이클은 Union-Find를 통해 판단한다.  
5) 문제는 마을을 2개로 분리하되 그 마을들도 최소가 되기를 원한다
-> 마지막에 추가되는 간선을 지우면 추가됐던 간선 중 가장 비용이 높은 간선이
지워짐과 동시에 하나의 신장트리가 두개로 나뉘어지므로
각각의 비용이 가장 최소인 신장트리 즉, 마을을 만들 수 있다
따라서, 모든 연산 후 가장 마지막에 추가된 간선을 제거한다(그 간선의 비용을 빼준다)

'''

# 4) 
def findP(get_node):
    if parent[get_node] == 0:
        return get_node  # 입력받은 노드의 부모정보가 없으면 본인이 루트노드
    
    # 부모 정보가 있으면 
    # 루트노드까지 깊은 탐색을 위해 재귀 실행
    res = findP(parent[get_node])
    parent[get_node] = res
    return res   # 가장 마지막 루트노드값을 저장하기 위해 res변수 이용 

def union(a,b,cost):
    # findP 함수를 통해 루트 노드를 찾고
    root_a = findP(a)
    root_b = findP(b)
    
    if root_a == root_b: # 둘의 루트노트가 같으면 싸이클이므로
        return 0 # 간선에 추가하지 않을거니까 비용을 전달하지 않는다 
    
    # 둘의 루트 노드가 다르면 최소신장트리에 추가할거니까 비용전달
    # 전달하기전 두 노드가 연결되었음을 parent배열에 저장
    parent[root_b] = root_a
    return cost
    

N,M = map(int,input().split()) 

edge = []
for _ in range(M): # 1) 길(간선) 정보 저장
    edge.append(list(map(int,input().split())))
    
# 2) 비용 기준 오름차순 정렬
edge.sort(key=lambda x: x[2] )

# 3) 비용이 적은 간선부터 신장트리에 들어갈 정점으로 선택
parent = [0] * (N+1)
ans = 0 # MST비용 
last = 0
max_cost = -21e8

for i in range(M):
    a,b,c = edge[i] # A집,B집,비용
    # 4) union-find를 이용해 싸이클 확인  
    need_cost = union(a,b,c)
    ans += need_cost
    max_cost = max(max_cost,need_cost)
    
    
    
# 5) 가장 마지막에 추가된 간선의 비용 제거
# 본인은 추가하지 않을 간선도 비용에 0으로 추가했기 때문에
# 가장 큰 값을 뺀다  
ans -= max_cost

print(ans)