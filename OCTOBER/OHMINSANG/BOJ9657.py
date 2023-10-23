"""
23 / 10 / 20 알고 스터디
돌 게임3
"""
import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
dp = [0] * 1001
dp[1], dp[2], dp[3], dp[4] = "SK", "CY", "SK", "SK"
stones = [1, 3, 4]

for i in range(5, n + 1):
    # 상근이가 돌을 먼저 가져가는 개수만큼 루프
    for s in stones:
        # 상근이가 돌을 가져가기 전에 남은 수의 dp가 창영이면
        # 돌 i 개의 dp는 상근이
        if dp[i - s] == "CY":
            dp[i] = "SK"
            break
        dp[i] = "CY"

print(dp[n])
