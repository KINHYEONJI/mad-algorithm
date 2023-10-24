n = int(input())
m = int(input())

arr = [0]*(41)
arr[1],arr[2] = 1,2
i = 3
while i < 41:
    arr[i] = arr[i-1] + arr[i-2]
    i += 1

vip = [0] + [int(input()) for _ in range(m)] + [n+1]
ans = 1
for i in range(m+1):
    a = vip[i+1]-vip[i]
    if a > 1:
        ans *= arr[a-1]
print(ans)