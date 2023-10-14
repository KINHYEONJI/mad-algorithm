#스택 나보다 작은건물 다 빼면 나를 볼 수 있는 건물 세는 양식
n = int(input())
 
arr = [int(input()) for i in range(n)]
stk = []
ans = 0
 
for i in range(n):
    while stk and stk[-1] <= arr[i]:
        stk.pop()
 
    stk.append(arr[i])
    ans += len(stk) -1
 
print(ans)