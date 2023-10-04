import sys
import heapq

input = sys.stdin.readline
n = int(input())

leftheap = []  # mid보다 작은 수들을 포함하는 최대힙
rightheap = []  # mid보다 큰 수들을 포함하는 최소힙

for _ in range(n):
    num = int(input())

    # 두 힙의 길이가 같으면 최대힙에 푸쉬
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -num)

    # 두 힙의 길이가 다르면 최소힙에 푸쉬
    else:
        heapq.heappush(rightheap, num)
    # 두 힙에 각각 원소가 존재하고, '최대힙의 루트*(-1)'가 '최소힙의 루트' 보다 더 크다면 루트들을 switch
    if len(leftheap) >= 1 and len(rightheap) >= 1 and -leftheap[0] > rightheap[0]:
        leftroot = heapq.heappop(leftheap)
        heapq.heappush(rightheap, -leftroot)

        rightroot = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -rightroot)

    print(-leftheap[0])