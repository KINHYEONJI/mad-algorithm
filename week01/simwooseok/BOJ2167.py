N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
k = int(input())
for i in range(k):
    i, j, x, y = map(int, input().split())
    Sum = 0
    for q in range(i-1, x):
        for l in range(j-1, y):
            Sum += arr[q][l]
    print(Sum)
