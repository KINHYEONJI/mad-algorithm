"""
23 / 11 / 06 알고 스터디
세 수의 합
"""
import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
arr = sorted([int(input()) for _ in range(n)])
lst = []

# x+y+z = k  -->   x+y = k-z
for i in range(n):
    for j in range(i, n):
        lst.append(arr[j] + arr[i])
lst.sort()

Max = 0
for i in range(n):
    for j in range(i, n):
        zk = arr[j] - arr[i]    # x+y+z = k  -->   x+y = k-z

        s = 0
        e = len(lst) - 1
        
        # 이분 탐색 시행
        while s <= e:
            mid = (s + e) // 2
            new = lst[mid]
            if zk > new: s = mid + 1
            elif zk < new: e = mid - 1
            else: Max = max(Max, arr[j]); break

print(Max)
