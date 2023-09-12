import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

high, low = 0, 0
Min, target = 10e10, lst[high] - lst[low]
while 1:
    if target >= m or high == n:
        low += 1
    elif target < m:
        high += 1

    if target >= m:
        Min = min(Min, target)
    elif low == n:
        break
print(Min)