import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    v,s,e = map(int,input().split())
    heapq.heappush(arr,[s,e])

r,c = heapq.heappop(arr)
ans = [c]
while arr:
    s,e = heapq.heappop(arr)
    if s < ans[0]:
        heapq.heappush(ans,e)
    else:
        heapq.heappop(ans)
        heapq.heappush(ans,e)
print(len(ans))