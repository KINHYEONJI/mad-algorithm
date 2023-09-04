"""
100 x 100 Matrix 생성
(3, 7) 부터 (13, 17)까지 1 입력
(15, 7)부터 (25, 17)까지 1 입력
(5, 2)부터 (15, 12)까지 1 입력
Matrix 내에서 값이 1 이상의 값 count
"""
arr = [[0] * 100 for _ in range(100)]
nums = int(input())
for i in range(nums):
    x_pot, y_pot = map(int, input().split())
    for x in range(x_pot, x_pot + 10):
        for y in range(y_pot, y_pot + 10):
            arr[x][y] = 1
cnt = 0
for x in range(100):
    for y in range(100):
        if arr[x][y] != 0:
            cnt += 1
print(cnt)
