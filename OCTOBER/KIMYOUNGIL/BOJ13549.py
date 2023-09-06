from collections import deque
n,k = map(int,input().split())
visited = [0]*100001

def bfs():
    q = deque()
    q.append([n,0])
    while q:
        p,c = q.popleft()
        if p == k:
            return print(c)
        
        if visited[p+1] == 0:
            visited[p+1] = 1
            q.append([p+1,c+1])
        if visited[p-1] == 0:
            visited[p-1] = 1
            q.append([p-1,c+1])

bfs()