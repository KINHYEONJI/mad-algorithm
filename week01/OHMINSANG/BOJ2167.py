'''
배열의 크기 n. m
n개의 줄 --> m개의 정수로 배열 주어짐
k = 합을 구할 부분의 개수
k개의 줄 --> 4개의 정수 i j x y
'''
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
"""
arr = [1, 2, 4],
      [8, 16, 32]]
"""
# 인덱스를 1부터 시작하기 위해 m+1, n +1 입력 // 누적합 계산하기.
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
"""
dp = [[0, 0, 0, 0],
      [0, 1, 3, 7],
      [0, 9, 27, 63]]
"""
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y]  -  dp[i - 1][y]  -  dp[x][j - 1]  +  dp[i - 1][j -1])


