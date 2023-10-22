n = int(input())
dp = [ i for i in range(n+1)]
dp[1] = 0
memo = [i for i in range(n+1)]
memo[1] = 0
for i in range(2, n+1):
    dp[i] = dp[i - 1] + 1
    memo[i] = i-1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i//3] + 1
        memo[i] = i//3
    if i % 2 == 0 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i//2]+1
        memo[i] = i//2


print(dp[n])
print(n,end=" ")

tmp = n
while memo[tmp] != 0:
    print(memo[tmp],end=" ")
    tmp = memo[tmp]