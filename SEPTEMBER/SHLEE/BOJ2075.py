# 1. 우선순위 큐
import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    numbers = list(map(int, input().split()))
    for num in numbers:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])

# 2. 슬라이싱
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
# for _ in range(n):
#     arr += list(map(int, input().split()))
#     arr = sorted(arr, reverse=True)[:n]
# print(arr[-1])