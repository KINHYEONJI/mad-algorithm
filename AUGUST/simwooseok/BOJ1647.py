N, M = map(int, input().split())
arr = [0] * (N+1)

def find(x):
    global arr
    if arr[x] == 0:
        return x
    ret = find(arr[x])
    arr[x] = ret
    return ret

def union(a, b, c):
    global arr, total, cnt
    xx , yy = find(a) , find(b)
    if xx == yy:
        return
    total+=c
    cnt +=1 
    arr[xx] = yy

total = 0 
cnt = 0
lst = [list(map(int, input().split())) for _ in range(M)]
lst2 = sorted(lst, key = lambda x : x[2])
for i in range(len(lst2)):
    if cnt == N-2: 
        print(total)
        break
    result = union(lst2[i][0],lst2[i][1],lst2[i][2])
