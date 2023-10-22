import sys
input=sys.stdin.readline
n=int(input())

dp = [0] *(n+1)
path = [0] *(n+1)

for i in range(2,n+1):
    dp[i] = dp[i-1] +1
    path[i] = i-1

    if i %2 == 0 and dp[i] > dp[i//2] +1:
        dp[i] = dp[i//2] +1
        path[i] = i //2

    if i % 3 == 0 and dp[i]>dp[i//3] +1:   #더 효율적인 연산 밑으로 오게 구성
        dp[i] = dp[i//3] +1
        path[i] = i //3

print(dp[n])
while n>0:
    print(n,end=' ')
    n = path[n]