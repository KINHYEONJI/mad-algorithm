n,m = map(int,input().split())
arr = [[0]*(m+1)] + [[0]+list(map(int,input())) for _ in range(n)]
dir = [[-1,0],[0,-1],[-1,-1]]
for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i][j] == 1:
            flag = 1
            val = []
            for k in range(3):
                dy = i + dir[k][0]
                dx = j + dir[k][1]
                if arr[dy][dx] == 0:
                    flag = 0
                    break
                else:
                    val.append(arr[dy][dx])

            if flag:
                arr[i][j] = min(val)+1
ans = 0
for i in arr:
    ans = max(max(i),ans)
print(ans**2)