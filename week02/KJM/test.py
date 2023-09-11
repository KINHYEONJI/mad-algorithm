import sys
sys.stdin = open('week02/KJM/input.txt','r')

def findP(node, parent):
    if parent[node] == node:
        return node
    
    parent[node] = findP(parent[node], parent)
    return parent[node]

def union(a, b, parent, rank):
    root_a = findP(a, parent)
    root_b = findP(b, parent)
    
    if root_a == root_b:
        return
    
    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
        if rank[root_a] == rank[root_b]:
            rank[root_b] += 1

def min_spanning_tree_cost(edges, n):
    edges.sort(key=lambda x: x["cost"])
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    total_cost = 0
    
    for edge in edges:
        a, b, cost = edge["a"], edge["b"], edge["cost"]
        if findP(a, parent) != findP(b, parent):
            union(a, b, parent, rank)
            total_cost += cost
    
    return total_cost

N, M = map(int, input().split())

edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append({"a": a, "b": b, "cost": cost})

# 분리된 마을 안에서의 최소 신장 트리를 구하는데, 모든 노드를 연결하므로 (N-1)개의 간선을 선택해야 함
min_cost = min_spanning_tree_cost(edges, N)
print(min_cost)
