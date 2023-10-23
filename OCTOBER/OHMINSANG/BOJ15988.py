"""
23 / 10 / 20 알고 스터디
1, 2, 3 더하기 3
"""
import sys
def input(): return sys.stdin.readline().rstrip()


T = int(input())
for TC in range(1,T+1):
    n = int(input())
    dp = [0]*1000001
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n+1):
        dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009
    print(dp[n])

"""
dp 인덱스 값 
#1 1
#2 2
#3 4

여기서 부터 n-1 n-2 n-3 의 합 == n
#4 7
#5 13

#6 24
#7 44
#8 81
#9 149
#10 274

#11 504
#12 927
#13 1705
#14 3136
#15 5768

"""