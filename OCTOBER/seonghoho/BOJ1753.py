import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

arr = [21e8] * (v + 1)
lst = [[] for _ in range(v + 1)]

for i in range(e):
    st, en, w = map(int, input().split())
    lst[st].append([en, w])


def dijk(start):
    global arr
    q = []
    heapq.heappush(q, (0, start))
    arr[start] = 0
    while q:
        Sum, now = heapq.heappop(q)
        if arr[now] < Sum: continue

        for i in lst[int(now)]:
            if arr[i[0]] < Sum + i[1]: continue
            arr[i[0]] = Sum + i[1]
            heapq.heappush(q,(arr[i[0]], i[0]))

dijk(k)

for i in range(1, v + 1):
    if arr[i] == 21e8:
        print('INF')
    else:
        print(arr[i])
