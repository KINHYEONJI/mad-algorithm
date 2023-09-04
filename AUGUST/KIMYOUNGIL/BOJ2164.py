from collections import deque

n = int(input())
q = deque()

for i in range(1,n+1):
    q.append(i)

if n == 1:
    print(q[0])

else:
    while 1:
        q.popleft()
        if len(q) == 1:
            print(q[0])
            break
        else:
            a = q.popleft()
            q.append(a)