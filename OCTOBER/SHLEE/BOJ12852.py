n = int(input())

dp = [0] * (n + 1)
ans = [n]
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])

ans = [n]
now = n
temp = dp[n] - 1
for i in range(n, 0, -1):
    if dp[i] == temp and (i + 1 == now or i * 2 == now or i * 3 == now):
        ans.append(i)
        temp -= 1
        now = i
print(*ans)
