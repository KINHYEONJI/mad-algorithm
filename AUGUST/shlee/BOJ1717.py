import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    return arr[x]

def union(a, b):
    global arr
    fa = find(a)
    fb = find(b)
    if fa == fb:
        return
    arr[fb] = fa


N, M = map(int, input().split())
arr = [i for i in range(N+1)]
for _ in range(M):
    k, a, b = map(int, input().split())
    if k == 0:
        union(a, b)
    elif k == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')