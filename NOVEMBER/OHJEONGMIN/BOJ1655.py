import heapq
import sys
input = sys.stdin.readline
n = int(input())
l_heap = []
r_heap = []
for i in range(n):
    if len(l_heap)==len(r_heap):
        heapq.heappush(l_heap,-int(input()))
    else:
        heapq.heappush(r_heap,int(input()))

    if r_heap:
        a = heapq.heappop(l_heap)
        b = heapq.heappop(r_heap)
        if -a>b:
            heapq.heappush(l_heap,-b)
            heapq.heappush(r_heap,-a)
        else:
            heapq.heappush(l_heap,a)
            heapq.heappush(r_heap,b)
    print(-l_heap[0])


