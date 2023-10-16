from collections import deque

n = int(input())
arr = [[] for _ in range(n+1)]
while 1:
    a,b = map(int,input().split())
    if a == -1 and b == -1: break
    arr[a].append(b)
    arr[b].append(a)

def bfs(x):
    user = [0]*(n+1)
    user[x] = 1
    q = deque()
    for i in arr[x]:
        user[i] = 1
        q.append([i,1])

    while q:
        p,c = q.popleft()
        for i in arr[p]:
            if user[i] == 0:
                user[i] = 1
                q.append([i,c+1])
    return c
  
ans = [0]*(n+1)
for i in range(1,n+1):
    ans[i] = bfs(i)

Min = min(ans[1:])
cnt = 0
p = []
for i in range(1,n+1):
    if ans[i] == Min:
        cnt += 1
        p.append(i)

print(Min, cnt)
print(*p)