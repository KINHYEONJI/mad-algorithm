# 우선순위 큐

import heapq
import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    heapq.heappush(lst,list(map(int,input().split())))

cnt = 0
computer = [0]*n
ans = [0]*n
while lst:
    start,end = heapq.heappop(lst)
    for i in range(n):
        if computer[i]<=start:
            if computer[i]==0:
                cnt+=1
            computer[i] = end
            ans[i]+=1
            break
print(cnt)
for i in ans:
    if i!=0:
        print(i,end=' ')

