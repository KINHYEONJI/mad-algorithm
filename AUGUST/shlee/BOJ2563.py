# 100x100 배열에서 색종이에 해당하는 부분을 1로 채우는 방법.
N = int(input())
arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1       # 한칸 당 넓이는 1

Sum = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            Sum += 1

print(Sum)