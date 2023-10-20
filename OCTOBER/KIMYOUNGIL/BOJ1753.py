import sys, heapq
input = sys.stdin.readline

v,e = map(int,input().split())
k = int(input())
arr = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    heapq.heappush(arr[a],[c,b])

def dik(start):
    q = []
    heapq.heappush(q, (0,start))
    result[start] = 0
    while q:
        x,p = heapq.heappop(q)
        if x > result[p]: continue
        for i in arr[p]:
            cost = x + i[0]
            if cost < result[i[1]]:
                result[i[1]] = cost
                heapq.heappush(q, (cost,i[1]))

result = [21e8]*(v+1)
dik(k)
for i in range(1,v+1):
    if result[i] == 21e8: print('INF')
    else: print(result[i])