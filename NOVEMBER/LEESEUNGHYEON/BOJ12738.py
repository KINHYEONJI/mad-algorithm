import sys

input = sys.stdin.readline

n = int(input())
lst = [-1000000001] + list(map(int, input().split()))
ans = [-1000000001]

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

print(len(ans) - 1)
