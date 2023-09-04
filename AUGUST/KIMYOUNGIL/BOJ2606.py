com = int(input())
n = int(input())
arr = [[] for _ in range(com+1)]
for i in range(n):
    s,e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)

cnt = 0
visited = [0]*(com+1)
def dfs(x):
    global cnt

    if arr[x] == []:
        return

    if arr[x] != []:
        for i in range(len(arr[x])):
            if visited[arr[x][i]] == 0:
                cnt += 1
                visited[arr[x][i]] = 1
                dfs(arr[x][i])

visited[1] = 1
dfs(1)
print(cnt)