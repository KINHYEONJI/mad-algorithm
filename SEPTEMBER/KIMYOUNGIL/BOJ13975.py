import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    arr = list(map(int,input().split()))
    heapq.heapify(arr)

    ans = 0
    while 1:
        if len(arr) == 1: break
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        ans += a+b
        heapq.heappush(arr,a+b)
    print(ans)