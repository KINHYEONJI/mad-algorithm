# 누적합의 개념이 필요한 문제(한번 계산한 결과는 다시 계산하지 않고 가져다 쓴다)
# i~j의 누적합을 구하는 방법 
# dp[i]가 i까지의 합이라고 했을 때
# i부터 j까지의 누적합은 dp[j] - dp[i-1] (dp[j]는 i의 값도 포함하기에 -1)

# 2차원 누적합(DP)를 만들고
# 주어진 좌표를 DP에서 찾아 계산한다

# 2차원 배열 누적합
# 위에서 구한 누적합 + 왼쪽에서 구한 누적합 - 교집합
'''
0 0 0 0
0 1 2 4
0 8 16 32 

1) 왼쪽 누적합
0 0 0 0
0 1 3 7
0 8 24 56 

2) 위에서 아래로 누적합
0 0 0 0
0 1 3 7
0 9 27 63
'''

# 누적합 개념 보고 다시 시도
n,m = map(int,input().split())   # n*m 배열
lsts = []
dp = [ [0] * (m+1) for _ in range(n+1)] # 세로가 n+1 가로가 m+1 인 dp배열 생성 

for _ in range(n): # 세로 n만큼 
    line = list(map(int,input().split())) # 입력 받아주고 
    
# dp 배열 생성
for i in range(1,n+1): # 세로 n+1
    for j in range(1,m+1): #가로 m+1
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + lsts[i-1][j-1]
# dp배열의 x,y좌표는 dp배열의 j~i 까지 누적합 + dp배열의 i~j 까지 누적합 - (누적합 중복 부분)  


# 시간초과 풀이
# N,M = map(int,input().split()) # 2, 3
# lsts = []  # N*M 배열

# for i in range(N):
#     line = list(map(int,input().split())) # 1 2 4 # 8 16 32
#     lsts.append(line)

# sum_cases = int(input())

# for case in range(sum_cases):
#     i,j,x,y = map(int,input().split())
    
#     sum_ = 0    
#     for row in range(i-1,x):
#         for col in range(j-1,y): 
#             sum_ += lsts[row][col]

#     print(sum_)