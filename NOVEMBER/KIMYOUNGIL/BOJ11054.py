n = int(input())
arr = list(map(int,input().split()))

result1 = [1]*n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            result1[i] = max(result1[i],result1[j]+1)

result2 = [1]*n
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if arr[i] > arr[j]:
            result2[i] = max(result2[i],result2[j]+1)

ans = [0]*n
for i in range(n):
    ans[i] = result1[i] + result2[i] - 1
print(max(ans))