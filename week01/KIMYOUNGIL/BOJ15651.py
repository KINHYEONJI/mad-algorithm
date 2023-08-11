n,m = map(int, input().split())
arr = list(range(1,n+1))
path = [0]*m
def dfs(x):
    if x == m:
        print(*path,sep=" ")
        return
    for i in range(n):
        path[x] = arr[i]
        dfs(x+1)

dfs(0)