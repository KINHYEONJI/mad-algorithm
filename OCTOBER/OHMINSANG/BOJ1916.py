import sys
sys.stdin = open('input.txt', 'r')

import heapq
from sys import maxsize

cities = int(input())
bus = int(input())

lst = [[] for _ in range(cities + 1)]
used = [maxsize] * (cities + 1) # maxsize는 무한대의 값 입력됨. 12e12랑 비슷한 역할

# 인접 리스트 만들기
for _ in range(bus):
    start, end, cost = map(int, input().split())
    lst[start].append([cost, end])

s, e = map(int, input().split())


def dijkstra(s):
    # heapq 생성 및 시작 위치를 heapq에 푸시
    hq = []
    heapq.heappush(hq, [0, s])
    used[s] = 0

    # heapq 순회
    while hq:
        cost, s = heapq.heappop(hq)

        # 백트래킹
        if used[s] < cost:
            continue

        # 현재 노드에서 다음 노드로 갈 때 비용을 계산하고, 비용이 더 낮은거를 선택해서 hq에 푸시
        for n_cost, e in lst[s]:
            Sum = cost + n_cost
            if used[e] > Sum:
                heapq.heappush(hq, (Sum, e))
                used[e] = Sum


dijkstra(s)
print(used[e])
