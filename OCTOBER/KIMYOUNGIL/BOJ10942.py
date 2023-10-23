import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().split())
m = int(input())

dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(1,n-i+1):
        a,b = j,i+j
        if a == b: dp[a][b] = 1
        elif b-a == 1 and arr[a-1] == arr[b-1]: dp[a][b] = 1
        elif dp[a+1][b-1] and arr[a-1] == arr[b-1]: dp[a][b] = 1

for _ in range(m):
    s,e = map(int,input().split())
    print(dp[s][e])