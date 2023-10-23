n = int(input())
arr = list(range(n+1))
arr[1] = 0
memo = list(range(n+1))
memo[1] = 0
for i in range(2,n+1):
    arr[i] = arr[i-1] + 1
    memo[i] = i-1

    if i%3 == 0 and arr[i] > arr[i//3] + 1:
        arr[i] = arr[i//3]+1
        memo[i] = i//3

    if i%2 == 0 and arr[i] > arr[i//2] + 1:
        arr[i] = arr[i//2]+1
        memo[i] = i//2

print(arr[n])

print(n,end=" ")
t = n
while memo[t]:
    print(memo[t],end=" ")
    t = memo[t]