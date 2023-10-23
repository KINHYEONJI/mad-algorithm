t = int(input())

dp = [0] * (1000000+ 1)


dp[0] = 1
dp[1] = 1
dp[2] = 2

# 1, 2, 3을 이용한 경우의 수를 계산
for i in range(3, 1000000 + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009 


for tc in range(t):
    n = int(input())
    print(dp[n])
