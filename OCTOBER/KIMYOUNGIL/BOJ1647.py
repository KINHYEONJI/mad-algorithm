import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
arr.sort(key= lambda x: x[2])

def boss(x):
    if lst[x] == 0: return x
    ret = boss(lst[x])
    lst[x] = ret
    return ret

def union(x,y):
    xb,yb = boss(x),boss(y)
    if xb == yb: return 0
    lst[yb] = xb
    return 1

lst = [0]*(n+1)
total = cnt = 0
for i in range(m):
    if cnt == n-2: break
    ret = union(arr[i][0],arr[i][1])
    if ret: cnt += 1; total += arr[i][2]

print(total)