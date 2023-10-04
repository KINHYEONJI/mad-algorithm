import sys
input = sys.stdin.readline

for _ in range(int(input())): 
    m,n,x,y = map(int,input().split())
    i = 0
    ans = -1
    if n == y: y = 0
    while 1:
        if (m*i+x)%n == y:
            ans = m*i+x
            break
        i += 1
        if m*i+x > m*n: break
    print(ans)