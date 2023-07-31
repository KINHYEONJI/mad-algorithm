h, m = map(int, input().split())
t = int(input())
mid = m + t
h_cnt = 0
if 0 <= mid <= 59:
    print(f'{h} {m+t}')
else:
    while mid >= 60:
        h_cnt += 1
        mid -= 60
    if (h+h_cnt) >= 24:
        h -= 24
    print(f'{h+h_cnt} {mid}')