def find(cycle):
    global arr
    if arr[cycle] == 0:
        return cycle

    ret = find(arr[cycle])
    arr[cycle] = ret
    return ret

def union(st, ed, cost):
    global arr , total
    xx , yy = find(st), find(ed)
    if xx == yy:
        return
    total += cost
    arr[xx] = yy
    return total

N = int(input())
M = int(input())
lst = [list(map(int, input().split())) for _ in range(M)]
lst.sort(key=lambda x: int(x[2]))
arr = [0] * (N + 1)
total = 0
for i in range(M):
    union(lst[i][0],lst[i][1],lst[i][2])
print(total)