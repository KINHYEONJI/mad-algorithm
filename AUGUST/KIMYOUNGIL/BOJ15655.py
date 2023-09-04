n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = [0]*m
def dfs(x,y):
    if x == m:
        print(*path,sep=" ")
        return
    for i in range(y,n):
        path[x] = arr[i]
        dfs(x+1,i+1)

dfs(0,0)