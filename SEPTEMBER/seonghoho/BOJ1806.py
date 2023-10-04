N, S = map(int, input().split())
lst = list(map(int, input().split()))

Min = 21e8
Sum = 0
low, high = 0, 0
cnt = 0
while 1:
    if Sum >= S or high == N:
        Sum -= lst[low]
        low += 1
        if cnt > 0:
            cnt -= 1
    else:
        Sum += lst[high]
        high += 1
        cnt += 1
    if Sum >= S:
        if Min > cnt:
            Min = cnt
    if low == N:
        break
if Min == 21e8 or S==0:
    print(0)
else:
    print(Min)