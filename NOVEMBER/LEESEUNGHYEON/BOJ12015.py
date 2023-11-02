import sys

input = sys.stdin.readline

n = int(input())
lst = [0] + list(map(int, input().split()))
ans = [0]

for i in range(1, n + 1):
    if lst[i] > ans[-1]:
        ans.append(lst[i])
    else:
        s, e = 0, len(ans) - 1
        while s < e:
            mid = (s + e) // 2
            if ans[mid] < lst[i]:
                s = mid + 1
            else:
                e = mid
        ans[e] = lst[i]     # 증가수열이 되면서 마지막 원소를 가장 작은수로 교체(나중에 더 많이 담을 수 있으므로)

print(len(ans) - 1)
