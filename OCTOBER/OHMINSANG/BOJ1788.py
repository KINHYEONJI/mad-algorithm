"""
23 / 10 / 20 알고 스터디
피보나치 수의 확장
"""

"""
-7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7  8  9  10
13 -8  5 -3  2 -1  1 0 1 1 2 3 5 8 13 21 34 55
"""

import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
nn = abs(n)

dp =[0]*1000001
dp[1] = 1
for i in range(2, nn+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000000

if n > 0:
    print(1)
elif n == 0:
    print(0)
elif nn % 2 == 1:
    print(1)
else:
    print(-1)
print(dp[nn])



