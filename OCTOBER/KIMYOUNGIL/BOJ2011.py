n = input()
m = len(n)
if n[0] == '0':print(0)
else:
    dp = [0]*(m+1)
    dp[0],dp[1] = 1,1
    for i in range(2,m+1):
        one = int(n[i-1])
        two = int(n[i-2])*10 + one
        if one: dp[i] += dp[i-1]
        if 10 <= two <= 26: dp[i] += dp[i-2]
    print(dp[m]%1000000)