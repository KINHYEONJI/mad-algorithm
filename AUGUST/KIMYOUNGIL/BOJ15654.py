n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = [0]*m
used = [0]*10000
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