N = int(input())
adj = [[] for i in range(N+1)]
for i in range(N):
    adj[i+1].append(int(input()))


def dfs(v,i):
    visited[v] = True

    for w in adj[v]:
        if not(visited[w]):
            dfs(w,i)
        elif visited[w] and w == i:
            result.append(w)

result = []
for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, i)
l = len(result)
print(l)
for i in range(l):
    print(result[i])
