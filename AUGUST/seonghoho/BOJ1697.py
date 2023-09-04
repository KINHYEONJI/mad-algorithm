'''
br = 3개, x-1, x+1, x*2
bfs 사용, 최소 cnt 구하기
'''
from collections import deque

N, K = map(int, input().split())
Max = 10**5
dist = [0]*(Max+1)

def bfs(now):
    q = deque()
    q. append(now)

    while q:
        now = q.popleft()
        if now == K:
            print(dist[now])
            break

        for i in (now-1, now+1, now*2):
            if 0<=i<=Max and dist[i]==0:
                dist[i] = dist[now] + 1
                q.append(i)

bfs(N)