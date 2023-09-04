def Chk(a, b):
    global arr
    fa, fb = find_bs(a), find_bs(b)
    if fa == fb:
        return 1


def find_bs(A):
    global arr
    if arr[A] == -1:
        return A
    ret = find_bs(arr[A])
    arr[A] = ret
    return ret


def union(a, b):
    global arr
    fa, fb = find_bs(a), find_bs(b)
    if fa == fb:
        return
    arr[fb] = fa


n, m = map(int, input().split())
lst = []
for i in range(m):
    lst.append(list(map(int, input().split())))
arr = [-1] * (n+1)  # arr을 0으로 초기화 할 경우 입력값이 0일 때 판독 못함.
for i in range(m):
    Select, x, y = lst[i]
    if Select == 0:
        union(x, y)
    else:
        ret = Chk(x, y)
        if ret == 1: print('YES')
        else: print('NO')