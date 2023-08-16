"""
카드2
버리고, 맨 뒤로 옮기고 반복
"""
from collections import deque

N = int(input())
q = deque()
for i in range(1, N + 1):
    q.append(i)
for i in range(N):
    if len(q) == 1:
        print(*q)
        break
    q.popleft()
    j = q.popleft()
    q.append(j)
