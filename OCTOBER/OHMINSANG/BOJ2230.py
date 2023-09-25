import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
lst = []
for _ in range(n): lst.append(int(input()))
lst.sort()
high, low = 0, 0
Min = 10e10
while 1:
    target = lst[high] - lst[low]
    if target >= m or high == n - 1:
        low += 1
    elif target < m:
        high += 1
    if target >= m: Min = min(Min, target)
    if low == n - 1: break
print(Min)
