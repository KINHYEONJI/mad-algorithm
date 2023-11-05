import sys

input = sys.stdin.readline

n = int(input())
lst = [0] + list(map(int, input().split()))
cnt = len(lst)
ans = [0]
for i in range(1, n + 1):
    if lst[i] > ans[-1]:
        ans.append(lst[i])
    else:
        s, e = 0, len(ans) - 1
        while s < e:
            mid = (s + e) // 2
            if lst[i] > ans[mid]:
                s = mid + 1
            else:
                e = mid
        ans[e] = lst[i]

print(cnt - len(ans))
