import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]
for i in range(m):
    s,e,p = map(int,input().split())
    arr[s].append([e,p])

start,end = map(int,input().split())
if start == end: print(0)
else:
    result = [21e8]*(n+1)
    result[start] = 0

    lst = []
    heapq.heapify(lst)
    
    for i in arr[start]:
        result[i[0]] = min(result[i[0]],i[1])
        heapq.heappush(lst,i)

    while lst:
        a = heapq.heappop(lst)
        if result[a[0]] < a[1]: continue
        for i in arr[a[0]]:
            if result[i[0]] > result[a[0]] + i[1]:
                result[i[0]] = result[a[0]] + i[1]
                heapq.heappush(lst,i)
    print(result[end])
