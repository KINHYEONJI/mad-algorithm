def find_bs(A):
    global arr
    if arr[A] == 0:
        return A
    ret = find_bs(arr[A])
    arr[A] = ret
    return ret


def union(a, b, cost):
    global arr, total, cnt, cost_lst
    fa, fb = find_bs(a), find_bs(b)
    if fa == fb:
        return
    total += cost
    cost_lst.append(cost)   # total에 cost 추가 할 때마다 리스트에 추가 된 값 작성
    cnt += 1
    arr[fb] = fa


n, m = map(int, input().split())
lst = []
cost_lst =[]
for i in range(m):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (x[2], x[0]))    # 내가 보기 편하게 2차정렬 기준 추가함.
arr = [0] * (n+1)
cnt = 0
total = 0

for i in range(m):
    x, y, price = lst[i]
    union(x, y, price)
print(total-cost_lst[-1])   # 집이 n-1, 1로 나뉠 때 최소값. 따라서 n에 대한 최소값 구하고 마지막 cost 빼기
