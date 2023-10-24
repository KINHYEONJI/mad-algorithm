"""
23 / 10 / 24 알고 스터디
도시 분할 계획
"""
import sys
def input(): return sys.stdin.readline().rstrip()


def find(A):
    global arr
    if arr[A] == 0:
        return A
    ret = find(arr[A])
    arr[A] = ret
    return ret


def union(a, b, cost):
    global arr, ans, cnt, cost_lst
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    ans += cost
    cost_lst.append(cost)
    cnt += 1
    arr[fb] = fa


n, m = map(int, input().split())
lst = []
cost_lst = []
for i in range(m):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (x[2], x[0]))
arr = [0] * (n + 1)
cnt, ans = 0, 0

for x, y, price in lst:
    union(x, y, price)

print(ans - cost_lst[-1])
