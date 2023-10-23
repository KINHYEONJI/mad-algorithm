import sys

input = sys.stdin.readline
n = int(input())
lst = [0] + [int(input()) for _ in range(n)]
dp = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])  # 안 밟는 경우
    dp[i][1] = dp[i - 1][0] + lst[i]  # 1번 연속 밟는 경우
    dp[i][2] = dp[i - 1][1] + lst[i]  # 2번 연속 밟는 경우

print(max(dp[n][1:3]))