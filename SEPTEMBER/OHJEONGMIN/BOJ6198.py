import sys
input = sys.stdin.readline
n = int(input())
lst = []
cnt = 0

for i in range(n):
    x = int(input())
    while lst:
        if lst[-1]<=x:
            lst.pop()
        else:
            cnt+=len(lst)
            lst.append(x)
            break
    else:
        cnt+=len(lst)
        lst.append(x)

print(cnt)