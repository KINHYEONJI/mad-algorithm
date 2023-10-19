import heapq, sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a].append([c,b])
    arr[b].append([c,a])
s,e = map(int,input().split())

result = [21e8]*(n+1)
def dik(start):
    q = []
    heapq.heappush(q,(0,start))
    result[start] = 0
    while q:
        x,p = heapq.heappop(q)
        if x > result[p]: continue
        for i in arr[p]:
            cost = x + i[0]
            if cost < result[i[1]]:
                result[i[1]] = cost
                heapq.heappush(q, (cost,i[1]))
dik(s)
print(result[e])