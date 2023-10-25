'''
모든 정점을 방문하면서 비용을 구해야하니 신장트리를 이용해야함
최소,최대 구분은 경로에 포함된 오르막길의 갯수 차이의 제곱으로 구한다
'''
n,m = map(int,input().split())
graph = [ [] for _ in range(n+1)]

def findR(get_node,parent):
    if parent[get_node] == -1:
        return get_node
    else:
        res = findR(parent[get_node],parent)
        parent[get_node] =res
        return res

def union(a,b,cost):
    root_a = findR(a,min_parent)
    root_b = findR(b,min_parent)

    if root_a == root_b:
        return 0

    else:
        min_parent[root_b] = root_a
        return cost

def max_union(a,b,cost):
    root_a = findR(a,max_parent)
    root_b = findR(b,max_parent)

    if root_a == root_b:
        return 0
    else:
        max_parent[root_b] = root_a
        return cost

info = []
for _ in range(m+1):
    # 계산의 편의를 위해 0(오르막길)을 ->1로
    # 1(내리막길)을 -> 0으로 바꿔서 저장한다
    v,w,tmp = map(int,input().split())
    c = abs(tmp-1)
    info.append([v,w,c])

min_info = sorted(info,key=lambda x:(x[2],x[0]) )
max_info = sorted(info,key=lambda x: (-x[2], x[0]) )

min_parent = [-1] * (n+1)
min_cost = 0
for v,w,c in min_info:
    min_cost += union(v,w,c)


max_parent = [-1] * (n+1)
max_cost = 0
for v,w,c in max_info:
    max_cost += max_union(v,w,c)

ans = (max_cost**2) - (min_cost**2)
print(ans)