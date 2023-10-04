from collections import deque

N, M = map(int, input().split())
arr = {}
for i in range(M):
    st, ed = map(int, input().split())
    if st not in arr:
        arr[st] = []
    if ed not in arr:
        arr[ed] = []
    arr[st].append(ed)
    arr[ed].append(st)


used = [0]* (N+1)
def bfs(start):
    dec = deque()
    dec.append(start)
    while dec:
        now = dec.popleft()
        if now not in arr: continue
        for neighbor in arr[now]:
            if used[neighbor] == 1: continue
            used[neighbor] = 1
            dec.append(neighbor)

cnt = 0
for i in range(1, N+1):
    if used[i] == 0 :
        used[i] = 1
        cnt +=1
        bfs(i)
print(cnt)