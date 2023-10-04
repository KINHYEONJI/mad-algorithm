import math

N = int(input())
used = [1] * 1000001
for i in range(2, int(math.sqrt(1000001)) + 1):
    if used[i] == 1:
        for j in range(2 * i, 1000001, i):
            used[j] = 0
ret = 0
for i in range(N, 1000001):
    if i == 1: continue
    if str(i) == str(i)[::-1]:
        if used[i] == 1:
            ret = i
            break

if ret == 0:
    print(1003001)
else:
    print(ret)
