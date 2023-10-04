n = int(input())
stack = list(map(int,input().split()))
ans,lst = [0]*n,[]
for i in range(n-1,-1,-1):
    while lst and stack[lst[-1]] < stack[i]: ans[lst.pop()] = i+1
    lst.append(i)
print(*ans)