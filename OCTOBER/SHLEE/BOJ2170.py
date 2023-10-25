import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[0]))
s, e = arr[0][0], arr[0][1]
ans = 0
for i in range(1, n):
    if arr[i][0] < e:
        if arr[i][1] > e:
            e = arr[i][1]
    else:
        ans += e - s
        s, e = arr[i][0], arr[i][1]

ans += e - s
print(ans)