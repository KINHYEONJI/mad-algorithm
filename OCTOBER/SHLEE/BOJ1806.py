import sys

input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 0, 0
summ = 0
minn = sys.maxsize
flag = 0
while end < N:
    summ += lst[end]
    while summ >= S:
        minn = min(minn, end - start + 1)
        flag = 1
        summ -= lst[start]
        start += 1
    end += 1

if flag:
    print(minn)
else:
    print(0)