def bossfind(a):
    global arr
    if arr[a]==0:
        return a
    ret = bossfind(arr[a])
    arr[a] = ret
    return ret

def union(x, y, i):
    global total, arr, cnt
    bossx, bossy = bossfind(x), bossfind(y)
    if bossx == bossy:
        return
    total += lst[i][2]
    cnt+= 1
    arr[bossy] = bossx

total = 0
cnt = 0

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
lst.sort(key=lambda x: x[2])
arr = [0] * (N + 1)
for i in range(M):
    if cnt == N-2:
        print(total)
        break
    union(lst[i][0], lst[i][1], i)