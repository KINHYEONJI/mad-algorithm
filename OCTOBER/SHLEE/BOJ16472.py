n = int(input())
lst = list(input())
start, end = 0, 0
cnt = 1
maxx = 0
used = set()
while start < len(lst) and end < len(lst):
    used.add(lst[start])
    if lst[end] not in used:
        cnt += 1
        used.add(lst[end])
    if cnt > n:
        cnt = 1
        start += 1
        used.clear()
        end = start
    ans = end - start + 1
    if ans > maxx:
        maxx = ans
    end += 1

print(maxx)
