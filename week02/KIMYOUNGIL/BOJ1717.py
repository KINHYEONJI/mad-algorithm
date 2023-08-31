import sys
input = sys.stdin.readline

def boss(x):
    if arr[x] == -1: return x
    ret = boss(arr[x])
    arr[x] = ret
    return ret

def union(x,y):
    xb,yb = boss(x),boss(y)
    if xb == yb: return
    arr[yb] = xb

n,m = map(int,input().split())
arr = [-1]*(n+1)
for _ in range(m):
    r,a,b = map(int,input().split())
    if r:
        if boss(a) == boss(b): print('YES')
        else: print('NO')
    else: union(a,b)