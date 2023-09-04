from collections import deque
def bfs(now):
    cnt=0
    q = deque()
    q.append(now)
    visited = [ 0 for _ in range(n+1)]
    visited[now] =1

    while q:
        x = q.popleft()
        for i in lst[x]:
            if visited[i]==0:
                visited[i]=1
                q.append(i)
                cnt+=1
    return cnt


n,m = map(int,input().split())
lst = [[] for _ in range(n+1)]
for i in range(m):
    s,e = map(int,input().split())
    lst[e].append(s)
Max = -21e8
result = []
for i in range(1,n+1):
    ret = bfs(i)
    if Max<ret:
        Max = ret
        result.clear()
        result.append(i)
    elif Max == ret:
        result.append(i)
result.sort()
print(*result)
