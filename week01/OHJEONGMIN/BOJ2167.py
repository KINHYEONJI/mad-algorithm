N,M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range (N)]
K = int(input())
arr = []
for i in range(K):
    row = list(map(int,input().split()))
    arr.append(row)
for h in range(K):
    Sum = 0
    i,j,x,y = arr[h][0],arr[h][1],arr[h][2],arr[h][3]
    for a in range(i-1,x):
        for b in range(j-1,y):
            Sum+=lst[a][b]
    print(Sum)