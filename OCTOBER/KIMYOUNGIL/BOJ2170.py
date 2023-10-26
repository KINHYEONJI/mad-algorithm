import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort()

ans = 0
a,b = -21e8,-21e8
for i,j in arr:
    if i > b:
        ans += j-i
        a,b = i,j
    else:
        if j <= b: continue
        else:
            ans += j-b
            b = j
print(ans)