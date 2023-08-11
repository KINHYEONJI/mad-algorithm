n,m = map(int, input().split())
arr = list(range(1,n+1))
path = [0]*m
used = [0]*(n+1)
def dfs(x):
    if x == m:
        print(*path,sep=" ")
        return
    for i in range(n):
        if used[i] == 0:
            used[i] = 1
            path[x] = arr[i]
            dfs(x+1)
            used[i] = 0

dfs(0)