import sys
sys.stdin = open('input.txt','r')
# N = 마을의 수 / M = 길의 수
N , M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
# unionfind로 두 집이 연결시켜준다
def find(x):
    global arr
    if arr[x] == 0:
        return x

    ret = find(arr[x])
    arr[x] = ret
    return ret


def union(x, y, Sum):
    global arr, total, cnt
    fx , fy = find(x) , find(y)
    if fx == fy:
        return
    total += Sum
    cnt += 1
    arr[fx] = fy

total = 0
cnt = 0
arr = [0] * (N+1)
lst2 = sorted(lst, key = lambda x : x[2])
for i in range(M):
    if cnt == N-2:
        print(total)
        break
    result = union(lst2[i][0], lst2[i][1] , lst2[i][2])
