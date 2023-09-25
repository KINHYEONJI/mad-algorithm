import heapq    # heapq 불러오기
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(input())
    lst = list(map(int, sys.stdin.readline().rstrip().split()))

    heap = []
    for i in range(N):  # 빈 heap 배열에 heapq로 lst의 수 넣기
        heapq.heappush(heap, lst[i])
    Sum = 0
    while len(heap) > 1:    # heap 리스트 안에 수가 하나 있을 때까지 while문 반복
        num1 = heapq.heappop(heap)  # 작은 두 수 꺼내서 더하기
        num2 = heapq.heappop(heap)
        Sum += num1 + num2
        heapq.heappush(heap, num1 + num2)   # 더한 수 다시 heap에 넣기
    print(Sum)