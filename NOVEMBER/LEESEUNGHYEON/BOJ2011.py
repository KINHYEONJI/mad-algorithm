lst = [0] + list(map(int, input()))

if lst[1] == 0:
    print(0)
    exit()

dp = [0] * (len(lst))
dp[0] = dp[1] = 1

for i in range(2, len(lst)):
    if lst[i] > 0:
        dp[i] += dp[i - 1]
    if 10 <= (lst[i - 1] * 10 + lst[i]) < 27:
        dp[i] += dp[i - 2]

    dp[i] %= 1000000

print(dp[len(lst) - 1])

