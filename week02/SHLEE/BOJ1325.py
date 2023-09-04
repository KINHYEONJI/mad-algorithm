from collections import deque

def bfs(n):
    q = deque()
    cnt = 0
    used = [0 for _ in range(N + 1)]
    q.append(n)
    used[n] = 1

    while q:
        nn = q.popleft()

        for k in arr[nn]:
            if used[k] == 1: continue
            used[k] = 1
            cnt += 1
            q.append(k)
    return cnt


N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)

lst = [0]
for i in range(1,N+1):
    ret = bfs(i)
    lst.append(ret)

for i in range(1,len(lst)):
    if lst[i] == max(lst):
        print(i,end=' ')
