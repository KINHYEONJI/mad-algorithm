import sys
input = sys.stdin.readline

def boss(x):
    if acc[x] == 0: return x
    ret = boss(acc[x])
    acc[x] = ret
    return ret

def union(a,b):
    fa,fb = boss(a),boss(b)
    if fa == fb: return 0
    acc[fb] = fa
    return 1

def abc():
    cnt = 0
    for i,j,k in arr:
        if union(i,j):
            cnt += 1-k
    return cnt

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m+1)]
arr.sort(key= lambda x:x[2])

acc = [0]*(n+1)
ret1 = abc()
arr.sort(key= lambda x:x[2], reverse=True)
acc = [0]*(n+1)
ret2 = abc()
print(ret1**2-ret2**2)