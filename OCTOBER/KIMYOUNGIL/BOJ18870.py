n = int(input())
arr = list(map(int,input().split()))

lst = []
for i in range(n):
    lst.append([arr[i],i])
lst.sort()

ans = [0]*n
for i in range(1,n):
    if lst[i-1][0] < lst[i][0]: ans[lst[i][1]] = ans[lst[i-1][1]] + 1
    else: ans[lst[i][1]] = ans[lst[i-1][1]]
print(*ans)