import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def find(n):
    global arr
    if arr[n] == 0:
        return n
    arr[n] = find(arr[n])
    return arr[n]


def union(a, b):
    global arr
    fa, fb = find(a), find(b)
    if fa == fb:
        return 1
    arr[fb] = fa


n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]
lst.sort(key=lambda x: x[2])
arr = [0] * (n + 1)
total, cnt = 0, 0
for i in range(m):

    ret = union(lst[i][0], lst[i][1])
    if not ret:
        cnt += 1
        total += lst[i][2]
    if cnt == n - 1:
        total -= lst[i][2]
        break

print(total)
