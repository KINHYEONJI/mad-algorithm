n, m = map(int, input().split())
def cb(a,b):
    cnt = 0
    while a > 0:
        a = a//b
        cnt += a
    return cnt
t,f = cb(n,2)-(cb(m,2)+cb(n-m,2)),cb(n,5)-(cb(m,5)+cb(n-m,5))
print(min(t,f))