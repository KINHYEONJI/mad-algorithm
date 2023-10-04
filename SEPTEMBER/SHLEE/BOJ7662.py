import sys
import heapq
input = sys.stdin.readline


test = int(input())
for _ in range(test):
    max_heap, min_heap = [], []
    visit = [0] * 1000001

    order_num = int(input())

    for key in range(order_num):
        order = input().split()
        if order[0] == 'I':
            heapq.heappush(min_heap, (int(order[1]), key))
            heapq.heappush(max_heap, (int(order[1]) * -1, key))
            visit[key] = 1 

        elif order[0] == 'D':
            if order[1] == '-1': 
                while min_heap and not visit[min_heap[0][1]]: 
                    heapq.heappop(min_heap) 
                if min_heap:
                    visit[min_heap[0][1]] = 0 
                    heapq.heappop(min_heap)
            elif order[1] == '1':
                while max_heap and not visit[max_heap[0][1]]: 
                if max_heap:
                    visit[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)


    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')