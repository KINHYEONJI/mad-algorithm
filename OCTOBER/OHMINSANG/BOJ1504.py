import sys, heapq

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    arr[s].append([cost, e])
    arr[e].append([cost, s])
inf = int(12e12)
pt1, pt2 = map(int, input().split())


def dijkstra(start, end):
    result = [inf] * (n + 1)
    hq = []
    heapq.heappush(hq, [0, start])
    result[start] = 0

    while hq:
        cost, k = heapq.heappop(hq)

        if cost > result[k]: continue

        for lst in arr[k]:
            new_cost = cost + lst[0]
            if new_cost < result[lst[1]]:
                result[lst[1]] = new_cost
                heapq.heappush(hq, [new_cost, lst[1]])
    return result[end]


ans = dijkstra(1, pt1)
ans += dijkstra(pt1, pt2)
ans += dijkstra(pt2, n)

Ans = dijkstra(1, pt2)
Ans += dijkstra(pt2, pt1)
Ans += dijkstra(pt1, n)

ans = min(ans, Ans)

if ans < inf and ans != 0:
    print(ans)
else:
    print(-1)
