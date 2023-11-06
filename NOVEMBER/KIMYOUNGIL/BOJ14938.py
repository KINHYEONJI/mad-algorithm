import heapq, sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    heapq.heappush(arr[a],(c,b))
    heapq.heappush(arr[b],(c,a))

v1,v2 = map(int,input().split())

path = [[1,v1,v2,n],[1,v2,v1,n]]

def dik(start,end):
    global res
    q = []
    heapq.heappush(q, (0,start))
    result[start] = 0
    while q:
        x,p = heapq.heappop(q)
        if p == end:
            res += x
            return 1
        
        for i in arr[p]:
            dist = x + i[0]
            if dist < result[i[1]]:
                result[i[1]] = dist
                heapq.heappush(q, (dist,i[1]))
    return 0

ans = 21e8
for i in range(2):
    res = 0
    for j in range(3):
        flag = 0
        result = [21e12]*(n+1)
        if dik(path[i][j],path[i][j+1]) == 0:
            flag = 1
            ans = -1
            break
    ans = min(ans,res)
print(ans)