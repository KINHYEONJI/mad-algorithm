import heapq, sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])
minH = []
seat = []
for i in range(1, n + 1):
    heapq.heappush(seat, i)
count = [0 for _ in range(n + 1)]
max_count = 0
for x in arr:
    while minH and x[0] >= minH[0][0]:
        end_time, s = heapq.heappop(minH)
        heapq.heappush(seat, s)
    s = heapq.heappop(seat)
    heapq.heappush(minH, [x[1], s])
    max_count = max(max_count, len(minH))
    count[s] += 1
print(max_count)
for i in range(1, max_count + 1):
    print(count[i], end=' ')
