n = int(input())
arr = list(map(int,input().split()))

result = [0]*n
for i in range(n):
    result[i] = arr[i]
    for j in range(i):
        if arr[i] > arr[j]:
            result[i] = max(result[i],result[j] + arr[i])
print(max(result))