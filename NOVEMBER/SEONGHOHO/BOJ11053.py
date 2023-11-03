N = int(input())
lst = list(map(int, input().split()))
num = [1] * N

for i in range(N):
    num1 = lst[i]
    for j in range(i):
        num2 = lst[j]
        if num1>num2:
            num[i] = max(num[i], num[j]+1)

print(max(num))