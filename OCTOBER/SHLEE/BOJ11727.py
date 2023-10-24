n = int(input())

dp = [0] * 1001
dp[1] = 1
for i in range(2, 1001):
    dp[i] = 2 ** i - dp[i - 1]
    dp[i] %= 10007
print(dp[n])