import sys, heapq
from collections import deque
input = sys.stdin.readline

n,m,k,s = map(int,input().split())
p,q = map(int,input().split())

zombie = [0]*(n+1)
for _ in range(k):
    zombie[int(input())] = 1

arr = [[] for _ in range(n+1)]
for _ in range(m):
    r,c = map(int,input().split())
    arr[r].append(c)
    arr[c].append(r)

def bfs():
    q = deque()
    for i in range(n+1):
        if zombie[i]: q.append([i,0])

    while q:
        p,c = q.popleft()
        if c < s:
            for i in arr[p]:
                if zombie[i] == 0:
                    zombie[i] = 2
                    q.append([i,c+1])
bfs()

price = [21e12]*(n+1)
def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0,start))
    price[start] = 0
    while heap:
        money, x = heapq.heappop(heap)
        if money > price[x]: continue
        for i in arr[x]:
            if zombie[i] == 0:
                cost = money + p

            elif zombie[i] == 1: continue
    
            elif zombie[i] == 2:
                cost = money + q

            if cost < price[i]:
                price[i] = cost
                heapq.heappush(heap, (cost,i))

dijkstra(1)
if zombie[n] == 2:
    print(price[n]-q)
else: 
    print(price[n]-p)