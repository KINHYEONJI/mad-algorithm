n,m = map(int, input().split())
arr = list(range(1,n+1))
path = [0]*m
# used = [0]*(n+1)
def dfs(x,y):
    if x == m:
        print(*path,sep=" ")
        return
    for i in range(y,n):
        # if used[i] == 0:
        path[x] = arr[i]
        dfs(x+1,i)
        # used[i] = 1

dfs(0,0)