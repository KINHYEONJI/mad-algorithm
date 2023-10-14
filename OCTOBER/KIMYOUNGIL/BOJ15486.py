import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [0]*(n+1)
t = 0
for i in range(n):
    t = max(t,dp[i])
    if i + arr[i][0] <= n:
        dp[i+arr[i][0]] = max(t+arr[i][1],dp[i+arr[i][0]])
print(max(dp))