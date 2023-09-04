n = int(input())

N = len(str(n))
arr = list(str(n))
count_lst = [0]*10

for i in range(N):
    count_lst[int(arr[i])] += 1

big = count_lst.index(max(count_lst[9],count_lst[6]))
minus = abs(count_lst[9] - count_lst[6])

if minus >= 2:
    count_lst[big] -= minus//2

print(max(count_lst))