import sys, heapq
input = sys.stdin.readline

n,m,k = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    heapq.heappush(arr[b],[c,a])
lst = list(map(int,input().split()))

def dik():
    q = []
    for i in lst:
        heapq.heappush(q, (0,i))
        result[i] = 0

    while q:
        x,p = heapq.heappop(q)
        if x > result[p]: continue
        for i in arr[p]:
            dis = x + i[0]
            if dis < result[i[1]]:
                result[i[1]] = dis
                heapq.heappush(q,(dis,i[1]))

result = [21e12]*(n+1)
dik()
print(result.index(max(result[1:])))
print(max(result[1:]))