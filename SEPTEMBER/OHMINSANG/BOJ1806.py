import sys

sys.stdin = open('input.txt', 'r')

n, s = map(int, input().split())
lst = list(map(int, input().split()))
high, low, Sum, length = 0, 0, lst[0], 1
Min = 10e10
while 1:
    if low == n:
        break
    if high == n - 1:
        if Sum >= s:
            Min = min(Min, length)
        length -= 1
        Sum -= lst[low]
        low += 1
        continue
    if Sum >= s:
        Min = min(Min, length)
        if high == n - 1 or high != low:
            length -= 1
            Sum -= lst[low]
            low += 1
        elif high == low:
            high += 1
            length += 1
            Sum += lst[high]
    elif Sum < s:
        high += 1
        Sum += lst[high]
        length += 1
if Min == 10e10:
    print(0)
elif Min <= 0:
    print(1)
else:
    print(Min)
