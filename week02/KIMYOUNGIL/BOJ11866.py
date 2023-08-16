from collections import deque
n,k = map(int,input().split())
q = deque()
for i in range(1,n+1):
    q.append(i)

lst = []
while q:
    for i in range(k-1):
        a = q.popleft()
        q.append(a)
    b = q.popleft()
    lst.append(b)
print('<',end="")
for i in range(n-1):
    print(f'{lst[i]}, ',end="")
print(lst[-1],end="")
print(">")