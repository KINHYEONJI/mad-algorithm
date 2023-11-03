N = int(input())
lst = list(map(int, input().split()))
res = [1] * N
for i in range(N):
    num1 = lst[i]
    for j in range(i):
        num2 = lst[j]
        if num1 < num2:
            res[i] = max(res[i], res[j] + 1)

print(max(res))
