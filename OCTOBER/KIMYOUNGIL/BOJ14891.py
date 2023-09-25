t = [list(map(int, input())) for _ in range(4)]
k = int(input())
arr = [list(map(int, input().split())) for _ in range(k)]

for i in range(k):
    lst = [0] * 4
    lst[arr[i][0] - 1] = arr[i][1]
    n = arr[i][0] - 1
    while 0 < n:
        if t[n - 1][2] == t[n][6]:
            break

        else:
            if lst[n] == -1:
                lst[n - 1] = 1
            else:
                lst[n - 1] = -1
            n -= 1

    n = arr[i][0] - 1
    while n < 3:
        if t[n][2] == t[n + 1][6]:
            break

        else:
            if lst[n] == -1:
                lst[n + 1] = 1
            else:
                lst[n + 1] = -1
            n += 1

    for i in range(4):
        if lst[i] == -1:
            a = t[i].pop(0)
            t[i].append(a)
        elif lst[i] == 1:
            b = t[i].pop()
            t[i].insert(0, b)

Sum = 0
for i in range(4):
    if t[i][0] == 1:
        Sum += 2 ** i

print(Sum)