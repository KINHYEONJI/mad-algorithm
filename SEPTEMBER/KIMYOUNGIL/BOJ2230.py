import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

def abc():
    ans,s,e = 21e8,0,0
    while 1:
        d = arr[e] - arr[s]
        if d == m: return print(m)
        elif m > d: e += 1
        else:
            s += 1
            ans = min(ans,d)
        if e == n:
            s += 1
            e = n-1
        if s == n-1: return print(ans)
abc()