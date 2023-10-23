import sys
input = sys.stdin.readline

tc = 1
while 1:
    n = int(input())
    if n == 0: break
    arr = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0]*3 for _ in range(n)]
    dp[1][0] = arr[0][1] + arr[1][0]
    dp[1][1] = min(arr[0][1],dp[1][0],arr[0][2]+arr[0][1]) + arr[1][1]
    dp[1][2] = min(arr[0][1],arr[0][1]+arr[0][2],dp[1][1]) + arr[1][2]
    for i in range(2,n):
        for j in range(3):
            if j == 0: Min = min(dp[i-1][j],dp[i-1][j+1])
            elif j == 1: Min = min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1],dp[i][j-1])
            else: Min = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
            dp[i][j] = Min + arr[i][j]
    print(f'{tc}. {dp[-1][1]}')
    tc += 1