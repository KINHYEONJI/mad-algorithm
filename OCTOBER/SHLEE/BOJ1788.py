n = int(input())
dp = [0] * 1000001
dp[1] = 1
for i in range(2, 1000000 + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= 1000000000

if n == 0:
    print(0)
    print(0)
elif n < 0 and abs(n) % 2 == 0:
    print(-1)
    print(dp[abs(n)])
else:
    print(1)
    print(dp[abs(n)])