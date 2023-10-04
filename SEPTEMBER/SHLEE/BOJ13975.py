import heapq
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)
    ans = 0
    while len(heap) > 1:
        temp1 = heapq.heappop(heap)
        temp2 = heapq.heappop(heap)
        ans += temp1 + temp2
        heapq.heappush(heap, temp1 + temp2)
    print(ans)