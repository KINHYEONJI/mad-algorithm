N,M = map(int,input().split())
arr = []
for i in range(N):
    row = list(map(int,input().split()))
    arr.append(row)

K = int(input())
for _ in range(K):
    i,j,x,y = map(int,input().split())
    Sum = 0
    for r in range(i,x+1):
        for c in range(j,y+1):
            Sum += arr[r-1][c-1]

    print(Sum)