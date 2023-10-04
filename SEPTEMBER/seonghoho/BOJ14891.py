from collections import deque

saw = [deque(map(int, input())) for _ in range(4)]
k = int(input())
how = []

for i in range(k):
    how.append(list(map(int, input().split())))
    how[i][0] -= 1

for a, b in how:
    tmp1 = saw[a][2]
    tmp2 = saw[a][6]
    k = b
    for i in range(a - 1, 0 - 1, -1):
        if saw[i][2] != tmp2:
            tmp2 = saw[i][6]
            saw[i].rotate(-1 * k)
            k *= -1
        else:
            break
    k = b
    for i in range(a + 1, 4):
        if saw[i][6] != tmp1:
            tmp1 = saw[i][2]
            saw[i].rotate(-1 * k)
            k *= -1
        else:
            break

    saw[a].rotate(b)
result = 0
for i in range(4):
    if saw[i][0] == 1:
        result += (2 ** i)
print(result)