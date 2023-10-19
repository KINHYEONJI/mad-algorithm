import sys,heapq
sys.stdin = open('input.txt','r')
#

n = int(input())
m = int(input())
graph = [ [] for _ in range(n+1) ]

for _ in range(m):
    s,e,c =  map(int,input().split())
    graph[s].append([e,c])

start,end = map(int,input().split())

INF = int(21e8)
distance = [INF] * (n+1)
route = [0] * (n+1)

def dijk(start):
    st_heap = []
    heapq.heappush(st_heap,(0,start))
    distance[start]= 0

    while st_heap:
        sofar_cost, now_node = heapq.heappop(st_heap)

        if distance[now_node] < sofar_cost: continue

        for next_node,next_cost in graph[now_node]:
            now_cost = sofar_cost + next_cost

            if now_cost < distance[next_node] or (now_cost == distance[next_node] and now_node < route[next_node]) :
                # 다음 노드의 비용정보에 저장된 값보다
                # 현재까지의 비용이 더 싸다
                # 다음노드의 비용 정보에 현재까지의 비용으로 갱신해주고
                distance[next_node] = now_cost
                # 다음노드의 경로 정보에 현재의 노드로 갱신해준다(최소경로니까)
                route[next_node] = now_node
                heapq.heappush(st_heap, (now_cost,next_node))

dijk(start)

# 경로 역추적한다
# route에 최소비용으로 갱신될 때 부모노드를 적어놨으니까...

ans = [end]
tmp = end
while tmp != start:
    tmp = route[tmp]
    ans.append(tmp)

ans.reverse()

print(distance[end])
print(len(ans))
print(*ans)