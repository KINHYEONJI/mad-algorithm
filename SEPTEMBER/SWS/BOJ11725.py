import sys
input=sys.stdin.readline
from collections import deque
N , M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    st, ed = map(int, input().split())
    arr[st].append(ed)
    arr[ed].append(st)


def bfs(start, arr):
    dec = deque()
    dec.append(start)
    check = [start]
    n = [0] * (N+1)
    while dec:
        now = dec.popleft()
        for neighbor in arr[now]:
            if neighbor not in check:
                n[neighbor] = n[now] +1
                check.append(neighbor)
                dec.append(neighbor)
    return sum(n)

Min = 3e13
cnt = 0
for i in range(1, N+1):
    ret = bfs(i, arr)
    if ret < Min:
        Min = ret
        cnt = i
print(cnt)




