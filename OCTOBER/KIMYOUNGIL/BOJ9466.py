import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x):
    global cnt
    visited[x] = 1
    res.append(x)

    if visited[arr[x]]:
        if arr[x] in res:
            cnt += len(res[res.index(arr[x]):])
        return
    else:
        dfs(arr[x])

for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int,input().split()))

    cnt = 0
    visited = [0]*(n+1)
    for i in range(1,n+1):
        if visited[i] == 0:
            res = []
            dfs(i)

    print(n-cnt)