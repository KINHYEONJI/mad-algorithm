import sys

input = sys.stdin.readline


def dfs(n, cnt):
    global ans

    if ans >= cnt + (N - n) * 2:    # 가지치기
        return

    if n == N:
        ans = max(ans, cnt)
        return

    if arr[n][0] <= 0:
        dfs(n + 1, cnt)
    else:
        flag = 0
        for j in range(N):
            if j == n or arr[j][0] <= 0: continue
            arr[j][0] -= arr[n][1]
            arr[n][0] -= arr[j][1]
            flag = 1
            dfs(n + 1, cnt + int(arr[j][0] <= 0) + int(arr[n][0] <= 0))
            arr[j][0] += arr[n][1]
            arr[n][0] += arr[j][1]
        if flag == 0:
            dfs(n + 1, cnt)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, 0)
print(ans)