n = int(input())
lst = list(map(int, input().split()))
stack = []
ans = []

for i in range(n):

    while stack:
        if stack[-1][1] >= lst[i]:
            ans.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()

    if not stack:
        ans.append(0)

    stack.append([i, lst[i]])

print(*ans)