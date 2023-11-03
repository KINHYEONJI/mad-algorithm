N = int(input())
lst = list(map(int, input().split()))
Sum = lst[:]

for i in range(N):
    num1 = lst[i]
    for j in range(i):
        num2 = lst[j]
        if num1 > num2:
            Sum[i] = max(Sum[i], Sum[j] + num1)

print(max(Sum))