n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

def dfs(x,lst):
    global Max
    if x == n:
        cnt = 0
        for i in lst:
            if i[0] <= 0: cnt += 1
        if cnt > Max: Max = cnt
        return

    for i in range(n):
        if x != i:
            if lst[x][0] > 0 and lst[i][0] > 0:
                lst[x][0] -= lst[i][1]
                lst[i][0] -= lst[x][1]
                dfs(x+1,lst)
                lst[x][0] += lst[i][1]
                lst[i][0] += lst[x][1]
            else: dfs(x+1,lst)

Max = 0
dfs(0,arr)
print(Max)