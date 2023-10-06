import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque(int(input()) for _ in range(n))
lst = []
ans = 0
while arr:
    p = arr.popleft()
    while lst and lst[-1] <= p:
        lst.pop()
    lst.append(p)
    ans += len(lst) - 1
print(ans)