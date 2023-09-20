import sys

sys.stdin = open("input.txt", "r")

import heapq
T = int(input())
for i in range(T):
    n = int(input())
    card = list(map(int, input().split()))
    heapq.heapify(card)

    ans = 0
    while len(card) > 1:
        temp1, temp2 = heapq.heappop(card), heapq.heappop(card)
        ans += (temp1 + temp2)
        heapq.heappush(card, temp1 + temp2)
    print(ans)
