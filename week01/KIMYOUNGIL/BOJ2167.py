n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
sum_point = [list(map(int, input().split())) for _ in range(k)]

for i in sum_point:
    x1,y1,x2,y2 = i

    sum = 0
    for j in range(x1-1,x2):
        for k in range(y1-1,y2):
            sum += arr[j][k]

    print(sum)