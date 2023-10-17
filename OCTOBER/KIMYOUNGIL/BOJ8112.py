from collections import deque
def bfs():
    q = deque(['1'])
    visit = [0]*n
    while q:
        p = q.popleft()
        a = int(p)%n
        if not a: return print(p)
        if visit[a]: continue
        visit[a] = 1
        q.append(p+'0')
        q.append(p+'1')
    return print('BRAK')

for _ in range(int(input())):
    n = int(input())
    bfs()