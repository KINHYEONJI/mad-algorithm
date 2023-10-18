from collections import deque
for _ in range(int(input())):
    n = int(input())
    q = deque(['1'])
    visit = [0]*n
    while q:
        p = q.popleft()
        a = int(p)%n
        if not a: print(p); break
        if visit[a]: continue
        visit[a] = 1
        q.append(p+'1')
        q.append(p+'0')