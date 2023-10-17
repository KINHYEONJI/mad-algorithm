import heapq
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])

heap = []
for i in range(n):
    heapq.heappush(heap, arr[i][0])
    if arr[i][1] < len(heap):
        heapq.heappop(heap)
print(sum(heap))
